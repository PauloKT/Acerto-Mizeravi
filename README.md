# Sistema de Quiz - Acerto Mizeravi

Sistema de quiz educacional desenvolvido em Flask com interface web moderna.

## 🚀 Funcionalidades

- **Sistema de Autenticação**: Login e registro de usuários
- **Quiz Interativo**: Sistema de perguntas com múltiplas opções
- **Categorias e Dificuldades**: Organização por temas e níveis
- **Perguntas Manuais**: Banco de perguntas personalizado
- **Interface Responsiva**: Design moderno e intuitivo
- **Sistema de Sons**: Efeitos sonoros para melhor experiência
- **Fallback Inteligente**: Funciona com ou sem banco de dados

## 📁 Estrutura do Projeto

```
├── app/
│   ├── data/           # Banco de perguntas manuais
│   ├── models/         # Modelos de dados (User, Quiz, Pergunta)
│   ├── routes/         # Rotas da API (auth, users, quiz)
│   └── services/       # Lógica de negócio
├── config/             # Configurações do sistema
├── static/             # Arquivos estáticos (HTML, CSS, JS)
├── tests/              # Testes do sistema
└── main.py            # Aplicação principal
```

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Banco de Dados**: MySQL (opcional, com fallback em memória)
- **Arquitetura**: MVC, API REST

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd Acerto-Mizeravi
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**
   ```bash
   python main.py
   ```

4. **Acesse no navegador**
   - Login: http://localhost:5000/
   - Menu: http://localhost:5000/menu
   - Quiz: http://localhost:5000/quiz
   - Registro: http://localhost:5000/register

## 🎮 Como Usar

1. **Registre-se** ou faça login
2. **Escolha** uma categoria e dificuldade
3. **Responda** as perguntas do quiz
4. **Veja** seus resultados e pontuação

## 📊 Sistema de Perguntas

O sistema possui perguntas organizadas por:
- **Categorias**: geral, historia, ciencias
- **Dificuldades**: easy, medium, hard
- **Quantidade**: 10-20 perguntas por quiz

### Adicionando Novas Perguntas

Edite o arquivo `app/data/perguntas.py` para adicionar novas perguntas:

```python
{
    "pergunta": "Sua pergunta aqui?",
    "opcoes": ["Opção A", "Opção B", "Opção C", "Opção D"],
    "resposta_correta": 0,  # Índice da resposta correta (0-3)
    "categoria": "sua_categoria"
}
```

## 🔧 Configuração

### Banco de Dados (Opcional)

Para usar MySQL, configure em `config/config.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'acerto_mizeravi',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'port': 3306,
    'charset': 'utf8mb4'
}
```

### Modo de Desenvolvimento

O sistema funciona em dois modos:
- **Com Banco**: Usa MySQL para persistência
- **Sem Banco**: Usa sistema em memória (fallback automático)

## 🎵 Recursos de Áudio

O sistema inclui efeitos sonoros:
- `click.mp3` - Som de clique
- `corret.wav` - Resposta correta
- `wrong.wav` - Resposta incorreta
- `gameover.mp3` - Fim do jogo
- `intro.mp3` - Música de fundo

## 🔒 Segurança

- Validação de dados no frontend e backend
- Sanitização de entradas
- Sistema de autenticação seguro
- Proteção contra SQL injection

## 📈 Melhorias Futuras

- [ ] Sistema de ranking global
- [ ] Estatísticas de desempenho
- [ ] Mais categorias de perguntas
- [ ] Sistema de conquistas
- [ ] Modo multiplayer
- [ ] API para mobile

## 🐛 Reportar Bugs

Encontrou um problema? Abra uma issue no repositório com:
- Descrição do problema
- Passos para reproduzir
- Screenshots (se aplicável)
- Informações do sistema

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👥 Contribuição

Contribuições são bem-vindas! Por favor:
1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

---

Paulo Henrique Amaral Martins
José Guilherme Oliveira Martins
Cristian Cesar De Lima Filho
João Victor Brandão
Gabriel Shinkae
Arthur Melquiades
Erick Costa
Heitor Santis Cortes
