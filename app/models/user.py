from datetime import datetime
from typing import Optional, Dict, Any

class User:
    def __init__(self, id: int, nome: str, email: str, data_registro: datetime):
        self.id = id
        self.nome = nome
        self.email = email
        self.data_registro = data_registro
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'data_registro': self.data_registro.isoformat() if hasattr(self.data_registro, 'isoformat') else str(self.data_registro)
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        return cls(
            id=data['id'],
            nome=data['nome'],
            email=data['email'],
            data_registro=data['data_registro']
        )
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, nome='{self.nome}', email='{self.email}')"