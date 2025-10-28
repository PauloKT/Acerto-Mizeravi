from typing import List, Optional
from app.models.user import User
from app.services.simple_user_service import simple_user_service

try:
    from config.database import get_db_connection
    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False

class UserService:
    """Serviço para operações com usuários"""
    
    @staticmethod
    def create_user(nome: str, email: str, login: str, senha: str) -> User:
        """Cria um novo usuário"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    
                    # Verificar se email ou login já existe
                    cursor.execute("SELECT id FROM usuarios WHERE email = %s OR login = %s", (email, login))
                    if cursor.fetchone():
                        raise ValueError("Este email ou login já está registrado.")
                    
                    # Inserir novo usuário
                    cursor.execute(
                        "INSERT INTO usuarios (nome, email, login, senha) VALUES (%s, %s, %s, %s)",
                        (nome, email, login, senha)
                    )
                    conn.commit()
                    
                    # Buscar o usuário criado
                    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (cursor.lastrowid,))
                    usuario_data = cursor.fetchone()
                    
                    return User(
                        usuario_data['id'],
                        usuario_data['nome'],
                        usuario_data['email'],
                        usuario_data['login'],
                        usuario_data['senha'],
                        usuario_data['data_registro']
                    )
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return simple_user_service.create_user(nome, email, login, senha)
    
    @staticmethod
    def authenticate_user(login: str, senha: str) -> Optional[User]:
        """Autentica usuário por login e senha"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    cursor.execute("SELECT * FROM usuarios WHERE login = %s AND senha = %s AND ativo = TRUE", (login, senha))
                    usuario_data = cursor.fetchone()
                    
                    if usuario_data:
                        return User(
                            usuario_data['id'],
                            usuario_data['nome'],
                            usuario_data['email'],
                            usuario_data['login'],
                            usuario_data['senha'],
                            usuario_data['data_registro']
                        )
                    return None
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return simple_user_service.authenticate_user(login, senha)
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Busca usuário por ID"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    cursor.execute("SELECT * FROM usuarios WHERE id = %s AND ativo = TRUE", (user_id,))
                    usuario_data = cursor.fetchone()
                    
                    if usuario_data:
                        return User(
                            usuario_data['id'],
                            usuario_data['nome'],
                            usuario_data['email'],
                            usuario_data['login'],
                            usuario_data['senha'],
                            usuario_data['data_registro']
                        )
                    return None
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return simple_user_service.get_user_by_id(user_id)
    
    @staticmethod
    def get_all_users() -> List[User]:
        """Lista todos os usuários"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    cursor.execute("SELECT * FROM usuarios WHERE ativo = TRUE ORDER BY data_registro DESC")
                    usuarios_data = cursor.fetchall()
                    
                    usuarios = []
                    for usuario_data in usuarios_data:
                        usuario = User(
                            usuario_data['id'],
                            usuario_data['nome'],
                            usuario_data['email'],
                            usuario_data['login'],
                            usuario_data['senha'],
                            usuario_data['data_registro']
                        )
                        usuarios.append(usuario)
                    
                    return usuarios
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return simple_user_service.get_all_users()
    
    @staticmethod
    def update_user(user_id: int, nome: str, email: str, login: str = None, senha: str = None) -> User:
        """Atualiza um usuário"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor(dictionary=True)
                    
                    # Verificar se usuário existe
                    cursor.execute("SELECT * FROM usuarios WHERE id = %s AND ativo = TRUE", (user_id,))
                    if not cursor.fetchone():
                        raise ValueError("Usuário não encontrado")
                    
                    # Verificar se email ou login já existe em outro usuário
                    if email:
                        cursor.execute("SELECT id FROM usuarios WHERE email = %s AND id != %s", (email, user_id))
                        if cursor.fetchone():
                            raise ValueError("Este email já está sendo usado por outro usuário.")
                    
                    if login:
                        cursor.execute("SELECT id FROM usuarios WHERE login = %s AND id != %s", (login, user_id))
                        if cursor.fetchone():
                            raise ValueError("Este login já está sendo usado por outro usuário.")
                    
                    # Construir query de atualização dinamicamente
                    campos = []
                    valores = []
                    
                    if nome:
                        campos.append("nome = %s")
                        valores.append(nome)
                    if email:
                        campos.append("email = %s")
                        valores.append(email)
                    if login:
                        campos.append("login = %s")
                        valores.append(login)
                    if senha:
                        campos.append("senha = %s")
                        valores.append(senha)
                    
                    if not campos:
                        raise ValueError("Nenhum campo para atualizar")
                    
                    valores.append(user_id)
                    query = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = %s"
                    
                    cursor.execute(query, valores)
                    conn.commit()
                    
                    # Buscar usuário atualizado
                    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
                    usuario_data = cursor.fetchone()
                    
                    return User(
                        usuario_data['id'],
                        usuario_data['nome'],
                        usuario_data['email'],
                        usuario_data['login'],
                        usuario_data['senha'],
                        usuario_data['data_registro']
                    )
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return simple_user_service.update_user(user_id, nome, email, login, senha)
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Deleta um usuário (soft delete)"""
        if DB_AVAILABLE:
            try:
                with get_db_connection() as conn:
                    cursor = conn.cursor()
                    
                    # Verificar se usuário existe
                    cursor.execute("SELECT id FROM usuarios WHERE id = %s AND ativo = TRUE", (user_id,))
                    if not cursor.fetchone():
                        raise ValueError("Usuário não encontrado")
                    
                    # Soft delete - marcar como inativo
                    cursor.execute("UPDATE usuarios SET ativo = FALSE WHERE id = %s", (user_id,))
                    conn.commit()
                    
                    return True
            except Exception as e:
                print(f"Erro no banco de dados: {e}")
                # Fallback para sistema em memória
                pass
        
        # Sistema em memória (fallback)
        return simple_user_service.delete_user(user_id)