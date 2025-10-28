"""
Configuração simplificada para desenvolvimento
"""
import os

# Configurações básicas da aplicação
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = True
    
    # Configurações de banco de dados (opcional)
    DB_CONFIG = {
        'host': os.environ.get('DB_HOST', 'localhost'),
        'database': os.environ.get('DB_NAME', 'acerto_mizeravi'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASSWORD', ''),
        'port': int(os.environ.get('DB_PORT', 3306)),
        'charset': 'utf8mb4',
        'collation': 'utf8mb4_unicode_ci'
    }
    
    # Configurações do quiz
    QUIZ_CONFIG = {
        'perguntas_por_quiz': {
            'easy': 10,
            'medium': 15,
            'hard': 20
        },
        'tempo_limite': None,  # Sem limite de tempo por padrão
        'tentativas_maximas': 1
    }
    
    # Configurações de segurança
    SECURITY_CONFIG = {
        'senha_minima': 4,
        'sessao_timeout': 3600,  # 1 hora
        'max_tentativas_login': 5
    }

# Configuração de desenvolvimento
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

# Configuração de produção
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-in-production'

# Configuração de teste
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DB_CONFIG = {
        'host': 'localhost',
        'database': 'acerto_mizeravi_test',
        'user': 'root',
        'password': '',
        'port': 3306,
        'charset': 'utf8mb4'
    }

# Configuração ativa
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}