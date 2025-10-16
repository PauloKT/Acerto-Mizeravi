from typing import List, Optional
from app.models.user import User
from config.database import get_db_connection

class UserService:
    
    @staticmethod
    def create_user(nome: str, email: str) -> User:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor(dictionary=True)
                
                # Verificar se email já existe
                cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
                if cursor.fetchone():
                    raise ValueError("Este email já está registrado.")
                
                # Inserir novo usuário
                cursor.execute(
                    "INSERT INTO usuarios (nome, email) VALUES (%s, %s)",
                    (nome, email)
                )
                conn.commit()
                
                # Buscar o usuário criado
                cursor.execute("SELECT * FROM usuarios WHERE id = %s", (cursor.lastrowid,))
                usuario_data = cursor.fetchone()
                
                return User(
                    usuario_data['id'],
                    usuario_data['nome'],
                    usuario_data['email'],
                    usuario_data['data_registro']
                )
        except Exception as e:
            raise Exception(f"Erro ao criar usuário: {e}")
    
    @staticmethod
    def get_user_by_name(nome: str) -> Optional[User]:
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND ativo = TRUE", (nome,))
                usuario_data = cursor.fetchone()
                
                if usuario_data:
                    return User(
                        usuario_data['id'],
                        usuario_data['nome'],
                        usuario_data['email'],
                        usuario_data['data_registro']
                    )
                return None
        except Exception as e:
            raise Exception(f"Erro ao buscar usuário: {e}")
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Busca usuário por ID"""
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
                        usuario_data['data_registro']
                    )
                return None
        except Exception as e:
            raise Exception(f"Erro ao buscar usuário: {e}")
    
    @staticmethod
    def get_all_users() -> List[User]:
        """Lista todos os usuários"""
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
                        usuario_data['data_registro']
                    )
                    usuarios.append(usuario)
                
                return usuarios
        except Exception as e:
            raise Exception(f"Erro ao listar usuários: {e}")
    
    @staticmethod
    def update_user(user_id: int, nome: str, email: str) -> User:
        """Atualiza um usuário"""
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor(dictionary=True)
                
                # Verificar se usuário existe
                cursor.execute("SELECT * FROM usuarios WHERE id = %s AND ativo = TRUE", (user_id,))
                if not cursor.fetchone():
                    raise ValueError("Usuário não encontrado")
                
                # Verificar se email já existe em outro usuário
                cursor.execute("SELECT id FROM usuarios WHERE email = %s AND id != %s", (email, user_id))
                if cursor.fetchone():
                    raise ValueError("Este email já está sendo usado por outro usuário.")
                
                # Atualizar usuário
                cursor.execute(
                    "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s",
                    (nome, email, user_id)
                )
                conn.commit()
                
                # Buscar usuário atualizado
                cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
                usuario_data = cursor.fetchone()
                
                return User(
                    usuario_data['id'],
                    usuario_data['nome'],
                    usuario_data['email'],
                    usuario_data['data_registro']
                )
        except Exception as e:
            raise Exception(f"Erro ao atualizar usuário: {e}")
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Deleta um usuário (soft delete)"""
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
            raise Exception(f"Erro ao deletar usuário: {e}")
