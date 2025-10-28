"""
Serviço de usuários simplificado para uso sem banco de dados
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.models.user import User

class SimpleUserService:
    """Serviço de usuários em memória para desenvolvimento"""
    
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1
    
    def create_user(self, nome: str, email: str, login: str, senha: str) -> User:
        """Cria um novo usuário"""
        # Verificar se email ou login já existe
        for usuario in self.usuarios:
            if usuario.email == email or usuario.login == login:
                raise ValueError("Este email ou login já está registrado.")
        
        # Criar novo usuário
        usuario = User(
            id=self.proximo_id,
            nome=nome,
            email=email,
            login=login,
            senha=senha,
            data_registro=datetime.utcnow()
        )
        
        self.usuarios.append(usuario)
        self.proximo_id += 1
        
        return usuario
    
    def authenticate_user(self, login: str, senha: str) -> Optional[User]:
        """Autentica usuário por login e senha"""
        for usuario in self.usuarios:
            if usuario.login == login and usuario.senha == senha:
                return usuario
        return None
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Busca usuário por ID"""
        for usuario in self.usuarios:
            if usuario.id == user_id:
                return usuario
        return None
    
    def get_user_by_login(self, login: str) -> Optional[User]:
        """Busca usuário por login"""
        for usuario in self.usuarios:
            if usuario.login == login:
                return usuario
        return None
    
    def get_all_users(self) -> List[User]:
        """Lista todos os usuários"""
        return self.usuarios.copy()
    
    def update_user(self, user_id: int, nome: str, email: str, login: str = None, senha: str = None) -> User:
        """Atualiza um usuário"""
        usuario = self.get_user_by_id(user_id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        
        # Verificar se email ou login já existe em outro usuário
        for u in self.usuarios:
            if u.id != user_id:
                if email and u.email == email:
                    raise ValueError("Este email já está sendo usado por outro usuário.")
                if login and u.login == login:
                    raise ValueError("Este login já está sendo usado por outro usuário.")
        
        # Atualizar campos
        if nome:
            usuario.nome = nome
        if email:
            usuario.email = email
        if login:
            usuario.login = login
        if senha:
            usuario.senha = senha
        
        return usuario
    
    def delete_user(self, user_id: int) -> bool:
        """Remove um usuário"""
        usuario = self.get_user_by_id(user_id)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False

# Instância global do serviço simplificado
simple_user_service = SimpleUserService()
