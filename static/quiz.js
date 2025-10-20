class QuizController {
    constructor() {
        this.usuarioId = this.gerarIdUsuario();
        this.quizAtivo = false;
        this.perguntaAtual = null;
        this.respostaSelecionada = null;
        this.pontuacao = 0;
        
        // Sons do jogo
        this.click = new Audio('sound/click.mp3');
        this.click.volume = 0.5;
        this.correct = new Audio('sound/corret.wav');
        this.correct.volume = 0.7;
        this.wrong = new Audio('sound/wrong.wav');
        this.wrong.volume = 0.7;
        
        this.initializeElements();
        this.bindEvents();
        this.carregarCategorias();
    }

    initializeElements() {
        // Elementos da tela de configuração
        this.configScreen = document.getElementById('config-screen');
        this.quantidadePerguntas = document.getElementById('quantidade-perguntas');
        this.categoriaSelect = document.getElementById('categoria');
        this.iniciarQuizBtn = document.getElementById('iniciar-quiz');

        // Elementos da tela do quiz
        this.quizScreen = document.getElementById('quiz-screen');
        this.pontuacaoAtual = document.getElementById('pontuacao-atual');
        this.perguntaAtualSpan = document.getElementById('pergunta-atual');
        this.totalPerguntasSpan = document.getElementById('total-perguntas');
        this.progressFill = document.getElementById('progress-fill');
        this.questionText = document.getElementById('question-text');
        this.optionsContainer = document.getElementById('options-container');
        this.responderBtn = document.getElementById('responder-pergunta');
        this.cancelarBtn = document.getElementById('cancelar-quiz');

        // Elementos da tela de resultados
        this.resultsScreen = document.getElementById('results-screen');
        this.resultsTitle = document.getElementById('results-title');
        this.finalScore = document.getElementById('final-score');
        this.scoreMessage = document.getElementById('score-message');
        this.novoQuizBtn = document.getElementById('novo-quiz');
        this.voltarMenuBtn = document.getElementById('voltar-menu');

        // Container de mensagens
        this.messageContainer = document.getElementById('message-container');
    }

    bindEvents() {
        this.iniciarQuizBtn.addEventListener('click', () => {
            this.playClickSound();
            this.iniciarQuiz();
        });
        this.responderBtn.addEventListener('click', () => {
            this.playClickSound();
            this.responderPergunta();
        });
        this.cancelarBtn.addEventListener('click', () => {
            this.playClickSound();
            this.cancelarQuiz();
        });
        this.novoQuizBtn.addEventListener('click', () => {
            this.playClickSound();
            this.novoQuiz();
        });
        this.voltarMenuBtn.addEventListener('click', () => {
            this.playClickSound();
            this.voltarMenu();
        });
    }

    gerarIdUsuario() {
        return 'user_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    playClickSound() {
        try {
            this.click.currentTime = 0;
            this.click.play().catch(() => {});
        } catch (e) {}
    }

    playCorrectSound() {
        try {
            this.correct.currentTime = 0;
            this.correct.play().catch(() => {});
        } catch (e) {}
    }

    playWrongSound() {
        try {
            this.wrong.currentTime = 0;
            this.wrong.play().catch(() => {});
        } catch (e) {}
    }

    async carregarCategorias() {
        try {
            const response = await fetch('/api/quiz/categorias');
            const data = await response.json();
            
            if (data.sucesso) {
                data.categorias.forEach(categoria => {
                    const option = document.createElement('option');
                    option.value = categoria;
                    option.textContent = categoria.charAt(0).toUpperCase() + categoria.slice(1);
                    this.categoriaSelect.appendChild(option);
                });
            }
        } catch (error) {
            console.error('Erro ao carregar categorias:', error);
        }
    }

    async iniciarQuiz() {
        try {
            this.mostrarMensagem('Iniciando quiz...', 'loading');
            
            const quantidade = parseInt(this.quantidadePerguntas.value);
            const categoria = this.categoriaSelect.value;

            const response = await fetch('/api/quiz/iniciar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    usuario_id: this.usuarioId,
                    quantidade_perguntas: quantidade
                })
            });

            const data = await response.json();

            if (data.sucesso) {
                this.quizAtivo = true;
                this.pontuacao = 0;
                this.perguntaAtual = data.pergunta;
                
                this.atualizarInterfaceQuiz();
                this.mostrarTelaQuiz();
                this.esconderMensagem();
            } else {
                this.mostrarMensagem(data.erro, 'error');
            }
        } catch (error) {
            this.mostrarMensagem('Erro ao iniciar quiz: ' + error.message, 'error');
        }
    }

    atualizarInterfaceQuiz() {
        if (!this.perguntaAtual) return;

        this.questionText.textContent = this.perguntaAtual.pergunta;
        this.perguntaAtualSpan.textContent = this.perguntaAtual.pergunta_atual;
        this.totalPerguntasSpan.textContent = this.perguntaAtual.total_perguntas;
        this.pontuacaoAtual.textContent = this.pontuacao;

        // Atualizar barra de progresso
        const progresso = (this.perguntaAtual.pergunta_atual - 1) / this.perguntaAtual.total_perguntas * 100;
        this.progressFill.style.width = progresso + '%';

        // Limpar opções anteriores
        this.optionsContainer.innerHTML = '';

        // Criar opções
        this.perguntaAtual.opcoes.forEach((opcao, index) => {
            const optionElement = document.createElement('div');
            optionElement.className = 'option';
            optionElement.textContent = opcao;
            optionElement.dataset.index = index;
            
            optionElement.addEventListener('click', () => this.selecionarOpcao(optionElement, index));
            
            this.optionsContainer.appendChild(optionElement);
        });

        this.respostaSelecionada = null;
        this.responderBtn.disabled = true;
    }

    selecionarOpcao(elemento, index) {
        // Remover seleção anterior
        document.querySelectorAll('.option').forEach(opt => {
            opt.classList.remove('selected');
        });

        // Selecionar nova opção
        elemento.classList.add('selected');
        this.respostaSelecionada = index;
        this.responderBtn.disabled = false;
    }

    async responderPergunta() {
        if (this.respostaSelecionada === null) return;

        try {
            this.responderBtn.disabled = true;
            this.mostrarMensagem('Processando resposta...', 'loading');

            const response = await fetch('/api/quiz/responder', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    usuario_id: this.usuarioId,
                    resposta: this.respostaSelecionada
                })
            });

            const data = await response.json();

            if (data.sucesso) {
                // Mostrar feedback visual da resposta
                this.mostrarFeedbackResposta(data.resposta_correta);

                if (data.quiz_finalizado) {
                    // Quiz finalizado
                    setTimeout(() => {
                        this.mostrarResultados(data.resultados);
                    }, 2000);
                } else {
                    // Próxima pergunta
                    setTimeout(() => {
                        this.perguntaAtual = data.proxima_pergunta;
                        this.pontuacao = data.pontuacao_atual;
                        this.atualizarInterfaceQuiz();
                        this.esconderMensagem();
                    }, 2000);
                }
            } else {
                this.mostrarMensagem(data.erro, 'error');
                this.responderBtn.disabled = false;
            }
        } catch (error) {
            this.mostrarMensagem('Erro ao responder pergunta: ' + error.message, 'error');
            this.responderBtn.disabled = false;
        }
    }

    mostrarFeedbackResposta(correta) {
        const opcoes = document.querySelectorAll('.option');
        const respostaCorreta = this.perguntaAtual.resposta_correta;

        // Tocar som baseado na resposta
        if (correta) {
            this.playCorrectSound();
        } else {
            this.playWrongSound();
        }

        opcoes.forEach((opcao, index) => {
            if (index === respostaCorreta) {
                opcao.classList.add('correct');
            } else if (index === this.respostaSelecionada && !correta) {
                opcao.classList.add('incorrect');
            }
        });

        // Desabilitar todas as opções
        opcoes.forEach(opcao => {
            opcao.style.pointerEvents = 'none';
        });
    }

    mostrarResultados(resultados) {
        this.quizAtivo = false;
        this.esconderMensagem();

        this.finalScore.textContent = `${resultados.pontuacao}/${resultados.total_perguntas}`;
        this.finalScore.className = 'final-score ' + this.getClassificacaoScore(resultados.porcentagem);

        this.scoreMessage.textContent = this.getMensagemScore(resultados.porcentagem);

        this.mostrarTelaResultados();
    }

    getClassificacaoScore(porcentagem) {
        if (porcentagem >= 90) return 'score-excellent';
        if (porcentagem >= 70) return 'score-good';
        if (porcentagem >= 50) return 'score-average';
        return 'score-poor';
    }

    getMensagemScore(porcentagem) {
        if (porcentagem >= 90) return 'Excelente! Você é um verdadeiro gênio! 🎉';
        if (porcentagem >= 70) return 'Muito bem! Você tem bons conhecimentos! 👏';
        if (porcentagem >= 50) return 'Bom trabalho! Continue estudando! 📚';
        return 'Não desista! Pratique mais e você melhorará! 💪';
    }

    async cancelarQuiz() {
        if (!this.quizAtivo) return;

        try {
            const response = await fetch('/api/quiz/cancelar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    usuario_id: this.usuarioId
                })
            });

            const data = await response.json();

            if (data.sucesso) {
                this.quizAtivo = false;
                this.mostrarTelaConfiguracao();
                this.mostrarMensagem('Quiz cancelado com sucesso', 'success');
            } else {
                this.mostrarMensagem(data.erro, 'error');
            }
        } catch (error) {
            this.mostrarMensagem('Erro ao cancelar quiz: ' + error.message, 'error');
        }
    }

    novoQuiz() {
        this.mostrarTelaConfiguracao();
        this.usuarioId = this.gerarIdUsuario();
    }

    voltarMenu() {
        window.location.href = 'menu.html';
    }

    mostrarTelaConfiguracao() {
        this.configScreen.classList.remove('hidden');
        this.quizScreen.classList.add('hidden');
        this.resultsScreen.classList.add('hidden');
    }

    mostrarTelaQuiz() {
        this.configScreen.classList.add('hidden');
        this.quizScreen.classList.remove('hidden');
        this.resultsScreen.classList.add('hidden');
    }

    mostrarTelaResultados() {
        this.configScreen.classList.add('hidden');
        this.quizScreen.classList.add('hidden');
        this.resultsScreen.classList.remove('hidden');
    }

    mostrarMensagem(mensagem, tipo = 'info') {
        this.messageContainer.innerHTML = `
            <div class="${tipo === 'loading' ? 'loading' : tipo === 'error' ? 'error-message' : 'success-message'}">
                ${mensagem}
            </div>
        `;
    }

    esconderMensagem() {
        this.messageContainer.innerHTML = '';
    }
}

// Inicializar o controller quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    new QuizController();
});
