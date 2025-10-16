from config import DB_CONFIG

def main():
    print("🔍 Testando conexão com MySQL...")
    print(f"📋 Configurações:")
    print(f"   Host: {DB_CONFIG['host']}")
    print(f"   Database: {DB_CONFIG['database']}")
    print(f"   User: {DB_CONFIG['user']}")
    print(f"   Port: {DB_CONFIG['port']}")
    print()
    
    if test_connection():
        print("✅ Conexão com MySQL funcionando!")
        
        # Testar se a tabela existe
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SHOW TABLES LIKE 'usuarios'")
                if cursor.fetchone():
                    print("✅ Tabela 'usuarios' encontrada!")
                    
                    # Contar usuários
                    cursor.execute("SELECT COUNT(*) FROM usuarios")
                    count = cursor.fetchone()[0]
                    print(f"📊 Total de usuários: {count}")
                else:
                    print("❌ Tabela 'usuarios' não encontrada!")
                    print("💡 Execute o script SQL no MySQL para criar as tabelas")
        except Exception as e:
            print(f"❌ Erro ao verificar tabelas: {e}")
    else:
        print("❌ Falha na conexão com MySQL!")
        print("💡 Verifique se:")
        print("   - MySQL está rodando")
        print("   - As configurações em config.py estão corretas")
        print("   - O banco de dados 'acerto_mizeravi' existe")

if __name__ == "__main__":
    main()