import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
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
