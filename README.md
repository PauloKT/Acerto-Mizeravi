# Acerto Mizeravi - Sistema de Usuários

Sistema completo de registro e login de usuários com interface web e API REST, desenvolvido em Flask com MySQL.

## 🚀 Funcionalidades

- ✅ **Interface Web** - Páginas de login e registro
- ✅ **API REST** - Endpoints completos para CRUD de usuários
- ✅ **Banco de Dados** - Integração com MySQL
- ✅ **Validação** - Validação robusta de dados
- ✅ **Estrutura Profissional** - Organização modular e escalável
- ✅ **Autenticação** - Sistema de login e registro

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

3. Configure o banco de dados:
   - Execute o script `database_schema.sql` no MySQL
   - Configure as credenciais em `config/config.py`

## 🚀 Como executar

1. Teste a conexão com o banco:
```bash
python tests/test_connection.py
```

2. Execute o servidor Flask:
```bash
python main.py
```

3. Acesse a aplicação:
   - **Login:** `http://localhost:5000`
   - **Registro:** `http://localhost:5000/register`

## 📚 Endpoints da API

### **Autenticação**
- **POST** `/api/registrar` - Registrar novo usuário
- **POST** `/api/login` - Login do usuário

### **Usuários**
- **GET** `/api/usuarios` - Listar todos os usuários
- **GET** `/api/usuarios/{id}` - Buscar usuário por ID
- **PUT** `/api/usuarios/{id}` - Atualizar usuário
- **DELETE** `/api/usuarios/{id}` - Deletar usuário

### **Exemplo de Registro:**
```json
POST /api/registrar
{
    "nome": "João Silva",
    "email": "joao@email.com"
}
```

### **Exemplo de Login:**
```json
POST /api/login
{
    "nome": "João Silva"
}
```

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
├── app/                    # Aplicação principal
│   ├── models/             # Modelos de dados
│   │   └── user.py         # Modelo de usuário
│   ├── routes/             # Rotas da API
│   │   ├── auth.py         # Autenticação
│   │   └── users.py        # CRUD de usuários
│   └── services/           # Lógica de negócio
│       └── user_service.py # Serviços de usuário
├── config/                 # Configurações
│   ├── config.py           # Configurações do banco
│   └── database.py          # Conexão com MySQL
├── static/                 # Arquivos estáticos
│   ├── index.html          # Página de login
│   ├── register.html       # Página de registro
│   ├── script.js           # JavaScript
│   └── style.css           # CSS
├── tests/                  # Testes
│   └── test_connection.py  # Teste de conexão
├── main.py                 # Aplicação principal
├── requirements.txt        # Dependências
└── database_schema.sql     # Script SQL
```

## 📊 Modelo de Dados

O sistema utiliza um modelo com os seguintes campos:

- **id**: Identificador único (gerado automaticamente)
- **nome**: Nome do usuário (obrigatório)
- **email**: Email do usuário (obrigatório, único)
- **data_registro**: Data e hora do registro (automático)
- **ativo**: Status do usuário (soft delete)

## 💾 Banco de Dados

- **MySQL**: Banco de dados principal
- **Tabela**: `usuarios` com índices otimizados
- **Conexão**: Pool de conexões com context manager
- **Transações**: Suporte completo a transações

## ⚠️ Validações

- Nome e email são obrigatórios
- Email deve ter formato válido
- Email deve ser único no sistema
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

## 🏗️ Arquitetura

### **Padrão MVC**
- **Models**: `app/models/user.py` - Modelo de dados
- **Views**: `static/` - Interface web
- **Controllers**: `app/routes/` - Lógica de controle

### **Separação de Responsabilidades**
- **Services**: Lógica de negócio isolada
- **Routes**: Apenas controle de requisições
- **Models**: Estrutura de dados
- **Config**: Configurações centralizadas

### **Vantagens da Estrutura**
- ✅ **Escalável** - Fácil adicionar novos recursos
- ✅ **Testável** - Cada camada pode ser testada isoladamente
- ✅ **Manutenível** - Código organizado e modular
- ✅ **Profissional** - Seguindo padrões da indústria

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.