# Sistema de Registro de Usuários

Sistema de backend para registro de usuários com nome e curso, desenvolvido em Flask.

## 🚀 Funcionalidades

- ✅ Registro de usuários com nome e curso
- ✅ Validação de dados de entrada
- ✅ Listagem de todos os usuários
- ✅ Busca de usuário por ID
- ✅ Atualização de dados do usuário
- ✅ Exclusão de usuários
- ✅ Armazenamento em memória (pronto para integração com banco)
- ✅ API REST completa

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd Acerto-Mizeravi
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como executar

1. Execute o servidor Flask:
```bash
python usuarios/register.py
```

2. O servidor estará disponível em: `http://localhost:5000`

## 📚 Endpoints da API

### 1. Teste da API
- **GET** `/api/teste`
- Retorna informações sobre os endpoints disponíveis

### 2. Registrar Usuário
- **POST** `/api/registrar`
- **Body:**
```json
{
    "nome": "João Silva",
    "curso": "Engenharia de Software"
}
```

### 3. Listar Usuários
- **GET** `/api/usuarios`
- Retorna lista de todos os usuários

### 4. Buscar Usuário por ID
- **GET** `/api/usuarios/{id}`
- Retorna dados de um usuário específico

### 5. Atualizar Usuário
- **PUT** `/api/usuarios/{id}`
- **Body:**
```json
{
    "nome": "João Silva Atualizado",
    "curso": "Engenharia de Software - Especialização"
}
```

### 6. Deletar Usuário
- **DELETE** `/api/usuarios/{id}`
- Remove um usuário do sistema

## 🧪 Testando a API

Execute o arquivo de exemplo para testar todos os endpoints:

```bash
python exemplo_uso_api.py
```

## 📝 Exemplos de Uso

### Registrar um usuário:
```bash
curl -X POST http://localhost:5000/api/registrar \
  -H "Content-Type: application/json" \
  -d '{"nome": "Maria Santos", "curso": "Ciência da Computação"}'
```

### Listar todos os usuários:
```bash
curl http://localhost:5000/api/usuarios
```

### Buscar usuário por ID:
```bash
curl http://localhost:5000/api/usuarios/1
```

## 🔧 Estrutura do Projeto

```
Acerto-Mizeravi/
├── usuarios/
│   └── register.py          # Servidor Flask principal
├── requirements.txt         # Dependências do projeto
├── exemplo_uso_api.py      # Exemplos de uso da API
└── README.md               # Este arquivo
```

## 📊 Modelo de Dados

O sistema utiliza um modelo simples com os seguintes campos:

- **id**: Identificador único (gerado automaticamente)
- **nome**: Nome do usuário (obrigatório, mínimo 2 caracteres)
- **curso**: Curso do usuário (obrigatório, mínimo 2 caracteres)
- **data_registro**: Data e hora do registro (automático)

## 💾 Armazenamento

- **Atual**: Dados armazenados em memória (lista Python)
- **Futuro**: Pronto para integração com qualquer banco de dados
- **Vantagem**: Estrutura preparada para migração fácil

## ⚠️ Validações

- Nome e curso são obrigatórios
- Nome e curso devem ter pelo menos 2 caracteres
- Dados são automaticamente limpos (trim) antes de salvar

## 🐛 Tratamento de Erros

A API retorna respostas padronizadas:

**Sucesso:**
```json
{
    "sucesso": true,
    "mensagem": "Operação realizada com sucesso",
    "dados": {...}
}
```

**Erro:**
```json
{
    "sucesso": false,
    "erro": "Descrição do erro",
    "detalhes": "Detalhes adicionais"
}
```

## 🔄 Integração Futura com Banco de Dados

O sistema está preparado para fácil integração com qualquer banco de dados:

### Estrutura Preparada
- Classe `Usuario` com métodos `to_dict()` e `buscar_por_id()`
- Lista `usuarios_db` que pode ser substituída por operações de banco
- Endpoints mantêm a mesma interface

### Exemplo de Migração (PostgreSQL)
```python
# Substituir a lista por:
import psycopg2
from psycopg2.extras import RealDictCursor

# Em cada endpoint, trocar:
# usuarios_db.append(usuario) → INSERT INTO usuarios...
# usuarios_db.remove(usuario) → DELETE FROM usuarios...
# [usuario.to_dict() for usuario in usuarios_db] → SELECT * FROM usuarios...
```

### Vantagens da Estrutura Atual
- ✅ Testes rápidos sem configuração de banco
- ✅ Desenvolvimento ágil
- ✅ Migração simples quando necessário
- ✅ Mesma API independente do armazenamento

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.