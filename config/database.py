import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
import os
import subprocess
from pathlib import Path
from .config import DB_CONFIG

@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        yield connection
    except Error as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def test_connection():
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"✅ Conectado ao MySQL versão: {version[0]}")
            return True
    except Error as e:
        print(f"❌ Erro na conexão: {e}")
        return False

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

def initialize_database():
    """
    Inicializa o banco de dados executando o arquivo database_schema.sql
    Inclui criação de tabelas, índices e triggers.
    Usa o cliente MySQL diretamente para suportar DELIMITER.
    """
    try:
        # Obter o caminho do arquivo SQL
        current_dir = Path(__file__).parent.parent
        sql_file = current_dir / 'database_schema.sql'
        
        if not sql_file.exists():
            print(f"⚠️  Arquivo SQL não encontrado: {sql_file}")
            return False
        
        print("📝 Executando schema SQL (com triggers)...")
        
        # Tentar usar o cliente MySQL diretamente (suporta DELIMITER)
        # Primeiro, tentar encontrar o executável mysql
        mysql_exe = None
        possible_paths = [
            'mysql',
            'C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe',
            'C:\\Program Files\\MySQL\\MySQL Server 8.4\\bin\\mysql.exe',
            'C:\\xampp\\mysql\\bin\\mysql.exe',
            'C:\\wamp64\\bin\\mysql\\mysql8.0.27\\bin\\mysql.exe',
        ]
        
        for path in possible_paths:
            try:
                result = subprocess.run(
                    [path, '--version'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    mysql_exe = path
                    break
            except:
                continue
        
        if mysql_exe:
            # Usar cliente MySQL diretamente
            cmd = [
                mysql_exe,
                f"-h{DB_CONFIG['host']}",
                f"-P{DB_CONFIG.get('port', 3306)}",
                f"-u{DB_CONFIG['user']}",
                f"-p{DB_CONFIG['password']}"
            ]
            
            try:
                with open(sql_file, 'r', encoding='utf-8') as f:
                    sql_content = f.read()
                
                result = subprocess.run(
                    cmd,
                    input=sql_content,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    # Verificar se os triggers foram criados
                    with get_db_connection() as conn:
                        cursor = conn.cursor()
                        cursor.execute("SHOW TRIGGERS")
                        triggers = cursor.fetchall()
                        
                        print(f"✅ Banco de dados inicializado com sucesso!")
                        print(f"📊 Triggers encontrados: {len(triggers)}")
                        for trigger in triggers:
                            print(f"   - {trigger[0]}")
                        cursor.close()
                    return True
                else:
                    print(f"⚠️  Erro ao executar SQL: {result.stderr}")
                    # Continuar para tentar método alternativo
            except subprocess.TimeoutExpired:
                print("⚠️  Timeout ao executar SQL via cliente MySQL")
            except Exception as e:
                print(f"⚠️  Erro ao usar cliente MySQL: {e}")
        
        # Método alternativo: executar via mysql.connector (sem DELIMITER)
        print("📝 Tentando método alternativo (via Python)...")
        
        base_config = DB_CONFIG.copy()
        if 'database' in base_config:
            base_config.pop('database')
        
        conn = mysql.connector.connect(
            host=base_config['host'],
            user=base_config['user'],
            password=base_config['password'],
            port=base_config.get('port', 3306),
            charset=base_config.get('charset', 'utf8mb4')
        )
        cursor = conn.cursor()
        
        # Ler o arquivo SQL
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Remover DELIMITER e processar statements manualmente
        lines = sql_content.split('\n')
        statements = []
        current_statement = []
        delimiter = ';'
        
        for line in lines:
            stripped = line.strip()
            
            # Ignorar comentários
            if not stripped or stripped.startswith('--'):
                continue
            
            # Detectar mudança de DELIMITER
            if stripped.upper().startswith('DELIMITER'):
                parts = stripped.split()
                if len(parts) > 1:
                    delimiter = parts[1]
                continue
            
            # Adicionar linha ao statement atual
            current_statement.append(line)
            
            # Se encontrou o delimiter atual no final da linha
            if stripped.endswith(delimiter):
                # Remover o delimiter do final
                stmt = '\n'.join(current_statement).rstrip()[:-len(delimiter)].strip()
                
                # Se estava usando //, adicionar ; no final para mysql.connector
                if delimiter == '//':
                    stmt += ';'
                
                if stmt:
                    statements.append(stmt)
                current_statement = []
                delimiter = ';'  # Resetar delimiter após usar
        
        # Adicionar último statement se houver
        if current_statement:
            stmt = '\n'.join(current_statement).strip()
            if stmt:
                if delimiter == '//':
                    stmt += ';'
                statements.append(stmt)
        
        # Executar statements
        for statement in statements:
            if not statement.strip():
                continue
            try:
                # Executar statement completo
                cursor.execute(statement)
                conn.commit()
            except Error as e:
                error_msg = str(e).lower()
                if "already exists" not in error_msg:
                    print(f"⚠️  Aviso: {e}")
                conn.rollback()
        
        cursor.close()
        conn.close()
        
        # Verificar triggers
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SHOW TRIGGERS")
            triggers = cursor.fetchall()
            
            print(f"✅ Banco de dados inicializado!")
            print(f"📊 Triggers encontrados: {len(triggers)}")
            for trigger in triggers:
                print(f"   - {trigger[0]}")
            cursor.close()
        
        return True
        
    except Error as e:
        print(f"❌ Erro ao inicializar banco de dados: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        return False