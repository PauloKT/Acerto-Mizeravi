# Configuração simplificada para desenvolvimento
# Este arquivo permite que o sistema funcione sem banco de dados

# Configurações do Flask
DEBUG = True
SECRET_KEY = 'dev-secret-key-change-in-production'

# Configurações do banco de dados (opcional)
DB_CONFIG = {
    'host': '127.0.0.1',        
    'database': 'acerto_mizeravi',  
    'user': 'root',            
    'password': 'Azousoluap1.ktt7337',            
    'port': 3306,             
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

# Modo de desenvolvimento (sem banco de dados)
DEVELOPMENT_MODE = True
USE_DATABASE = False  # Mude para True quando tiver o MySQL configurado
