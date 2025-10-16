import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import mysql.connector
from config.config import DB_CONFIG

def test_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            port=DB_CONFIG.get('port', 3306)
        )
        print("✅ Conexão bem-sucedida!")
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"❌ Erro na conexão: {err}")
        return False

def main():
    print("🔍 Testando conexão com MySQL...")
    print(f"📋 Configurações:\n   Host: {DB_CONFIG['host']}\n   Database: {DB_CONFIG['database']}\n   User: {DB_CONFIG['user']}\n   Port: {DB_CONFIG.get('port', 3306)}\n")
    
    if test_connection():
        print("💡 Tudo certo!")
    else:
        print("💡 Verifique as configurações!")

if __name__ == "__main__":
    main()