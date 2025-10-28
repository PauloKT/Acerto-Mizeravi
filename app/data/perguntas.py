"""
Banco de dados de perguntas manuais para o quiz
"""
from typing import List, Dict, Any
from app.models.quiz import Pergunta
import random

# Banco de perguntas organizadas por categoria e dificuldade
PERGUNTAS_DB = {
    "humanas": {
        "easy": [
               {
                   "pergunta": "Quem é considerado o pai da filosofia ocidental?",
                   "opcoes": ["Sócrates", "Aristóteles", "Platão", "Descartes"],
                   "resposta_correta": 0,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Qual é o nome da famosa peça de Shakespeare sobre um príncipe dinamarquês?",
                   "opcoes": ["Macbeth", "Hamlet", "Romeu e Julieta", "Otelo"],
                   "resposta_correta": 1,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Em que século ocorreu o Renascimento na Europa?",
                   "opcoes": ["Século XIV", "Século XV", "Século XVI", "Século XVII"],
                   "resposta_correta": 1,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Quem escreveu \"O Príncipe\", um tratado sobre poder político?",
                   "opcoes": ["Maquiavel", "Rousseau", "Voltaire", "Locke"],
                   "resposta_correta": 0,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Qual movimento artístico enfatizava a emoção e a natureza no século XIX?",
                   "opcoes": ["Barroco", "Romantismo", "Classicismo", "Impressionismo"],
                   "resposta_correta": 1,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Quem é o autor de \"Dom Quixote\"?",
                   "opcoes": ["Miguel de Cervantes", "Dante Alighieri", "Victor Hugo", "Goethe"],
                   "resposta_correta": 0,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Qual filósofo defendeu a ideia de \"tabula rasa\"?",
                   "opcoes": ["Platão", "Kant", "John Locke", "Hegel"],
                   "resposta_correta": 2,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Em que país surgiu o teatro grego antigo?",
                   "opcoes": ["Itália", "Grécia", "Egito", "Roma"],
                   "resposta_correta": 1,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Quem pintou \"A Última Ceia\"?",
                   "opcoes": ["Michelangelo", "Rafael", "Leonardo da Vinci", "Botticelli"],
                   "resposta_correta": 2,
                   "categoria": "humanas"
               },
            {
                   "pergunta": "Qual é o principal tema da obra \"1984\" de George Orwell?",
                   "opcoes": ["Amor proibido", "Totalitarismo", "Viagem no tempo", "Magia"],
                   "resposta_correta": 1,
                   "categoria": "humanas"
               }
        ],
        "medium": [
            {
                "pergunta": "Qual escola filosófica grega defendia o prazer moderado como bem supremo?",
                "opcoes": ["Estoicismo", "Epicureísmo", "Cinismo", "Ceticismo"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem escreveu \"A Divina Comédia\"?",
                "opcoes": ["Virgílio", "Petrarca", "Dante Alighieri", "Boccaccio"],
                "resposta_correta": 2,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual movimento artístico surgiu na França no século XIX com foco na luz e cor?",
                "opcoes": ["Surrealismo", "Cubismo", "Impressionismo", "Expressionismo"],
                "resposta_correta": 2,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem é conhecido como o \"pai da psicanálise\"?",
                "opcoes": ["Jung", "Freud", "Adler", "Skinner"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Em que período histórico ocorreu a Reforma Protestante?",
                "opcoes": ["Idade Antiga", "Idade Média", "Renascimento", "Iluminismo"],
                "resposta_correta": 2,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual filósofo escreveu \"Assim Falou Zaratustra\"?",
                "opcoes": ["Nietzsche", "Schopenhauer", "Kierkegaard", "Heidegger"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem pintou \"Guernica\", uma crítica à guerra?",
                "opcoes": ["Dalí", "Picasso", "Miró", "Kandinsky"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual é o tema central da obra \"O Banquete\" de Platão?",
                "opcoes": ["Justiça", "Amor", "Política", "Conhecimento"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem é o autor de \"Crime e Castigo\"?",
                "opcoes": ["Tolstói", "Dostoiévski", "Tchekhov", "Gogol"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual movimento filosófico enfatizava a razão no século XVIII?",
                "opcoes": ["Existencialismo", "Empirismo", "Iluminismo", "Positivismo"],
                "resposta_correta": 2,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem esculpiu a estátua de David?",
                "opcoes": ["Donatello", "Bernini", "Michelangelo", "Rodin"],
                "resposta_correta": 2,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual é o principal conceito de \"O Ser e o Nada\" de Sartre?",
                "opcoes": ["Existencialismo", "Materialismo", "Idealismo", "Nihilismo"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Em que país surgiu o Expressionismo alemão?",
                "opcoes": ["França", "Alemanha", "Itália", "Espanha"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem escreveu \"A República\"?",
                "opcoes": ["Aristóteles", "Sócrates", "Platão", "Epicuro"],
                "resposta_correta": 2,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual artista é associado ao Cubismo analítico?",
                "opcoes": ["Braque", "Matisse", "Van Gogh", "Monet"],
                "resposta_correta": 0,
                "categoria": "humanas"
            }
        ],
        "hard": [
            {
                "pergunta": "Qual filósofo grego defendia a teoria das formas eternas?",
                "opcoes": ["Sócrates", "Aristóteles", "Platão", "Demócrito"],
                "resposta_correta": 2,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem é o autor de \"A Metamorfose\"?",
                "opcoes": ["Camus", "Kafka", "Sartre", "Beckett"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual movimento artístico do século XX explorava o subconsciente?",
                "opcoes": ["Futurismo", "Surrealismo", "Dadaísmo", "Minimalismo"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem desenvolveu a teoria do \"contrato social\" no século XVIII?",
                "opcoes": ["Hobbes", "Rousseau", "Montesquieu", "Voltaire"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual é o título da principal obra de Immanuel Kant sobre ética?",
                "opcoes": ["Crítica da Razão Pura", "Crítica da Razão Prática", "Fenomenologia do Espírito", "Ser e Tempo"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem pintou \"As Meninas\"?",
                "opcoes": ["Goya", "Velázquez", "El Greco", "Murillo"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual filósofo é conhecido pela frase \"Penso, logo existo\"?",
                "opcoes": ["Descartes", "Spinoza", "Leibniz", "Hume"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem escreveu \"Ulisses\", uma obra modernista?",
                "opcoes": ["Woolf", "Joyce", "Faulkner", "Proust"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual é o foco principal do Existencialismo?",
                "opcoes": ["Liberdade individual", "Determinismo", "Materialismo dialético", "Positivismo lógico"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem esculpiu \"O Pensador\"?",
                "opcoes": ["Rodin", "Brancusi", "Moore", "Giacometti"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual teoria filosófica de Hegel envolve tese, antítese e síntese?",
                "opcoes": ["Dialética", "Fenomenologia", "Hermenêutica", "Pragmatismo"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem é o autor de \"O Estrangeiro\"?",
                "opcoes": ["Camus", "Sartre", "Beauvoir", "Merleau-Ponty"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual movimento artístico enfatizava a abstração geométrica?",
                "opcoes": ["Fauvismo", "Suprematismo", "Art Nouveau", "Rococo"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem escreveu \"Crítica da Razão Pura\"?",
                "opcoes": ["Kant", "Hegel", "Schopenhauer", "Nietzsche"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual é o tema central de \"A Condição Humana\" de Hannah Arendt?",
                "opcoes": ["Política", "Arte", "Ciência", "Religião"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem pintou \"A Persistência da Memória\"?",
                "opcoes": ["Magritte", "Dalí", "Ernst", "Tanguy"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual filósofo defendeu o \"eterno retorno\"?",
                "opcoes": ["Nietzsche", "Kierkegaard", "Husserl", "Bergson"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem é o autor de \"O Grande Gatsby\"?",
                "opcoes": ["Hemingway", "Fitzgerald", "Steinbeck", "Faulkner"],
                "resposta_correta": 1,
                "categoria": "humanas"
            },
            {
                "pergunta": "Qual movimento filosófico surgiu com Wittgenstein?",
                "opcoes": ["Filosofia analítica", "Estruturalismo", "Pós-modernismo", "Fenomenologia"],
                "resposta_correta": 0,
                "categoria": "humanas"
            },
            {
                "pergunta": "Quem esculpiu \"Pietà\"?",
                "opcoes": ["Bernini", "Michelangelo", "Donatello", "Cellini"],
                "resposta_correta": 1,
                "categoria": "humanas"
            }
        ]
    },
    "exatas": {
        "easy": [
            {
                "pergunta": "Quanto é 2 + 2?",
                "opcoes": ["3", "4", "5", "6"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a forma geométrica com 4 lados iguais?",
                "opcoes": ["Triângulo", "Quadrado", "Círculo", "Pentágono"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Quanto é 5 x 3?",
                "opcoes": ["15", "8", "2", "10"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o número que vem depois de 10?",
                "opcoes": ["9", "11", "12", "13"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a unidade de medida de comprimento?",
                "opcoes": ["Litro", "Metro", "Quilograma", "Segundo"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Quanto é 10 - 4?",
                "opcoes": ["6", "14", "5", "7"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o resultado de 20 ÷ 4?",
                "opcoes": ["4", "5", "6", "8"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o nome do número 1000?",
                "opcoes": ["Cem", "Mil", "Dez", "Milhões"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Quantos lados tem um triângulo?",
                "opcoes": ["3", "4", "5", "6"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é 1 + 1 + 1?",
                "opcoes": ["2", "3", "4", "1"],
                "resposta_correta": 1,
                "categoria": "exatas"
            }
        ],
        "medium": [
            {
                "pergunta": "Qual é a fórmula da área de um círculo?",
                "opcoes": ["πr²", "2πr", "r²", "πr"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Quanto é a raiz quadrada de 16?",
                "opcoes": ["2", "3", "4", "5"],
                "resposta_correta": 2,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o valor de π aproximado?",
                "opcoes": ["3.14", "2.71", "1.61", "4.67"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Em física, qual é a unidade de força?",
                "opcoes": ["Joule", "Newton", "Watt", "Volt"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o resultado de 8²?",
                "opcoes": ["16", "32", "64", "128"],
                "resposta_correta": 2,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a fórmula da velocidade?",
                "opcoes": ["Distância / Tempo", "Tempo / Distância", "Massa x Aceleração", "Força / Área"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Quanto é 3/4 de 100?",
                "opcoes": ["50", "75", "25", "100"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o elemento químico com símbolo H?",
                "opcoes": ["Hélio", "Hidrogênio", "Oxigênio", "Carbono"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a lei de Newton sobre inércia?",
                "opcoes": ["Primeira", "Segunda", "Terceira", "Quarta"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Quanto é o logaritmo de 100 na base 10?",
                "opcoes": ["1", "2", "3", "4"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a unidade de energia?",
                "opcoes": ["Joule", "Pascal", "Ampere", "Ohm"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o resultado de sen(90°)?",
                "opcoes": ["0", "1", "-1", "Infinito"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Quanto é 2^3?",
                "opcoes": ["4", "6", "8", "16"],
                "resposta_correta": 2,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a fórmula da densidade?",
                "opcoes": ["Massa / Volume", "Volume / Massa", "Força / Massa", "Energia / Tempo"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o número atômico do carbono?",
                "opcoes": ["4", "6", "8", "12"],
                "resposta_correta": 1,
                "categoria": "exatas"
            }
        ],
        "hard": [
            {
                "pergunta": "Qual é a derivada de x²?",
                "opcoes": ["x", "2x", "x²", "2"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a constante de Planck?",
                "opcoes": ["6.626 x 10^-34", "3 x 10^8", "9.81", "1.38 x 10^-23"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a equação de Schrödinger?",
                "opcoes": ["E = mc²", "iħ ∂ψ/∂t = Hψ", "F = ma", "PV = nRT"],
                "resposta_correta": 1,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o teorema de Pitágoras?",
                "opcoes": ["a² + b² = c²", "a + b = c", "a/b = c", "a - b = c"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a velocidade da luz no vácuo?",
                "opcoes": ["3 x 10^8 m/s", "3 x 10^6 m/s", "3 x 10^10 m/s", "3 x 10^4 m/s"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a integral de 1/x?",
                "opcoes": ["ln|x|", "x²/2", "e^x", "sin x"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a lei de Ohm?",
                "opcoes": ["V = IR", "P = VI", "E = IR", "I = V/R"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o número de Avogadro?",
                "opcoes": ["6.022 x 10^23", "3.14 x 10^2", "9.8 x 10^0", "1.67 x 10^-27"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a fórmula da relatividade?",
                "opcoes": ["E = mc²", "E = mv²/2", "E = mgh", "E = qV"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o pH de uma solução neutra?",
                "opcoes": ["7", "0", "14", "1"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a constante gravitacional?",
                "opcoes": ["6.674 x 10^-11", "1.38 x 10^-23", "8.85 x 10^-12", "5.67 x 10^-8"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o teorema fundamental do cálculo?",
                "opcoes": ["Integra derivada", "Derivada integral", "Limite zero", "Série infinita"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a carga do elétron?",
                "opcoes": ["-1.6 x 10^-19 C", "1.6 x 10^-19 C", "9.1 x 10^-31 kg", "1.67 x 10^-27 kg"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a lei de Boyle?",
                "opcoes": ["PV = constante", "V/T = constante", "P/T = constante", "n = constante"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o momento de inércia de uma esfera?",
                "opcoes": ["(2/5)MR²", "MR²", "(1/2)MR²", "(1/3)MR²"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a equação de Dirac?",
                "opcoes": ["(iγ^μ ∂_μ - m)ψ = 0", "∇·E = ρ/ε", "F = G m1 m2 / r²", "h f = E"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a constante de Boltzmann?",
                "opcoes": ["1.38 x 10^-23", "6.626 x 10^-34", "9.81", "3 x 10^8"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é o princípio de Heisenberg?",
                "opcoes": ["Incerteza", "Exclusão", "Equivalência", "Conservação"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a fórmula de Euler?",
                "opcoes": ["e^{iπ} + 1 = 0", "a + bi = 0", "sin² + cos² = 1", "1 + 1 = 2"],
                "resposta_correta": 0,
                "categoria": "exatas"
            },
            {
                "pergunta": "Qual é a constante de Stefan-Boltzmann?",
                "opcoes": ["5.67 x 10^-8", "8.31", "6.02 x 10^23", "1.6 x 10^-19"],
                "resposta_correta": 0,
                "categoria": "exatas"
            }
        ]
    },
    "biologicas": {
        "easy": [
            {
                "pergunta": "Qual é o órgão responsável pela respiração?",
                "opcoes": ["Coração", "Pulmões", "Fígado", "Estômago"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o processo pelo qual as plantas fazem comida?",
                "opcoes": ["Respiração", "Fotossíntese", "Digestão", "Circulação"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Quantos ossos tem o corpo humano adulto?",
                "opcoes": ["206", "300", "150", "100"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o maior órgão do corpo humano?",
                "opcoes": ["Coração", "Pele", "Cérebro", "Fígado"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual gás as plantas absorvem do ar?",
                "opcoes": ["Oxigênio", "Dióxido de carbono", "Nitrogênio", "Hidrogênio"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a unidade básica da vida?",
                "opcoes": ["Átomo", "Célula", "Molécula", "Tecido"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual animal é conhecido como rei da selva?",
                "opcoes": ["Elefante", "Leão", "Tigre", "Girafa"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o sangue transportado pelas artérias?",
                "opcoes": ["Oxigenado", "Desoxigenado", "Nutrientes", "Hormônios"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o sentido responsável pelo olfato?",
                "opcoes": ["Visão", "Audição", "Olfato", "Tato"],
                "resposta_correta": 2,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o principal componente da água?",
                "opcoes": ["H2O", "CO2", "O2", "N2"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            }
        ],
        "medium": [
            {
                "pergunta": "Qual é o processo de divisão celular?",
                "opcoes": ["Mitose", "Meiose", "Ambas", "Nenhuma"],
                "resposta_correta": 2,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o nome do ácido no estômago?",
                "opcoes": ["HCl", "H2SO4", "NaOH", "HNO3"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o reino das plantas?",
                "opcoes": ["Animalia", "Plantae", "Fungi", "Protista"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a função dos ribossomos?",
                "opcoes": ["Síntese de proteínas", "Armazenamento", "Energia", "Transporte"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o tipo de reprodução em bactérias?",
                "opcoes": ["Sexual", "Assexual", "Ambas", "Nenhuma"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o hormônio do crescimento?",
                "opcoes": ["Insulina", "GH", "Adrenalina", "Testosterona"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o número de cromossomos humanos?",
                "opcoes": ["23", "46", "48", "22"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o processo de evolução por Darwin?",
                "opcoes": ["Seleção natural", "Mutação", "Hibridização", "Clonagem"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o órgão que filtra o sangue?",
                "opcoes": ["Rins", "Fígado", "Baço", "Pâncreas"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a vitamina da visão?",
                "opcoes": ["A", "B", "C", "D"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o tipo de sangue universal doador?",
                "opcoes": ["A", "B", "AB", "O"],
                "resposta_correta": 3,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o filo dos humanos?",
                "opcoes": ["Chordata", "Arthropoda", "Mollusca", "Annelida"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o enzima da saliva?",
                "opcoes": ["Amilase", "Lipase", "Pepsina", "Tripsina"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o ciclo do nitrogênio?",
                "opcoes": ["Fixação", "Todas", "Ammonificação", "Nitrificação"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o habitat das tartarugas marinhas?",
                "opcoes": ["Terra", "Água", "Ambos", "Ar"],
                "resposta_correta": 2,
                "categoria": "biologicas"
            }
        ],
        "hard": [
            {
                "pergunta": "Qual é a estrutura do DNA?",
                "opcoes": ["Dupla hélice", "Simples", "Tripla", "Quadrupla"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o processo de transcrição?",
                "opcoes": ["DNA a RNA", "RNA a proteína", "Proteína a DNA", "RNA a DNA"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a teoria da endossimbiose?",
                "opcoes": ["Origem de mitocôndrias", "Origem de núcleo", "Origem de ribossomos", "Origem de lisossomos"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o ciclo de Krebs?",
                "opcoes": ["Respiração celular", "Fotossíntese", "Fermentação", "Glicólise"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o número de pares de base no genoma humano?",
                "opcoes": ["3 bilhões", "1 bilhão", "5 bilhões", "2 bilhões"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o hormônio antidiurético?",
                "opcoes": ["ADH", "FSH", "LH", "TSH"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a lei de Hardy-Weinberg?",
                "opcoes": ["Equilíbrio genético", "Mutação", "Seleção", "Migração"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o tipo de mutação silenciosa?",
                "opcoes": ["Não altera proteína", "Altera", "Deleta", "Insere"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o órgão da hemodiálise?",
                "opcoes": ["Rins", "Fígado", "Coração", "Pulmões"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a vitamina K função?",
                "opcoes": ["Coagulação", "Visão", "Ossos", "Imunidade"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o filo das esponjas?",
                "opcoes": ["Porifera", "Cnidaria", "Platyhelminthes", "Nematoda"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o processo de apoptose?",
                "opcoes": ["Morte celular programada", "Divisão", "Fusão", "Migração"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o ciclo do carbono?",
                "opcoes": ["Fotossíntese e respiração", "Apenas fotossíntese", "Apenas respiração", "Nenhum"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a classe das aves?",
                "opcoes": ["Aves", "Mammalia", "Reptilia", "Amphibia"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o enzima da replicação DNA?",
                "opcoes": ["DNA polimerase", "RNA polimerase", "Helicase", "Ligase"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é a síndrome de Down cromossomo?",
                "opcoes": ["Trissomia 21", "Trissomia 18", "Monossomia X", "Trissomia 13"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o tipo de ligação em proteínas?",
                "opcoes": ["Peptídica", "Glicosídica", "Éster", "Fosfodiéster"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o bioma da Amazônia?",
                "opcoes": ["Floresta tropical", "Savana", "Deserto", "Tundra"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o vírus do HIV?",
                "opcoes": ["Retrovírus", "Adenovírus", "Herpesvírus", "Papilomavírus"],
                "resposta_correta": 0,
                "categoria": "biologicas"
            },
            {
                "pergunta": "Qual é o mecanismo de defesa imune?",
                "opcoes": ["Anticorpos", "Todas", "Linfócitos", "Macrófagos"],
                "resposta_correta": 1,
                "categoria": "biologicas"
            }
        ]
    },
    "geografia": {
        "easy": [
            {
                "pergunta": "Qual é a capital do Brasil?",
                "opcoes": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"],
                "resposta_correta": 2,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o maior oceano do mundo?",
                "opcoes": ["Atlântico", "Pacífico", "Índico", "Ártico"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Quantos continentes existem?",
                "opcoes": ["5", "6", "7", "8"],
                "resposta_correta": 2,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o rio mais longo do mundo?",
                "opcoes": ["Nilo", "Amazonas", "Mississipi", "Yangtzé"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital da França?",
                "opcoes": ["Berlim", "Paris", "Londres", "Madrid"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o menor país do mundo?",
                "opcoes": ["Mônaco", "Vaticano", "San Marino", "Liechtenstein"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o deserto mais quente?",
                "opcoes": ["Saara", "Atacama", "Kalahari", "Gobi"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a montanha mais alta?",
                "opcoes": ["K2", "Everest", "Kilimanjaro", "Aconcágua"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital da Austrália?",
                "opcoes": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                "resposta_correta": 2,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o continente mais frio?",
                "opcoes": ["Ásia", "Antártica", "Europa", "África"],
                "resposta_correta": 1,
                "categoria": "geografia"
            }
        ],
        "medium": [
            {
                "pergunta": "Qual é a capital do Canadá?",
                "opcoes": ["Toronto", "Ottawa", "Vancouver", "Montreal"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o maior país em área?",
                "opcoes": ["China", "Rússia", "EUA", "Brasil"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o rio que passa por Paris?",
                "opcoes": ["Tâmisa", "Sena", "Danúbio", "Reno"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país com mais população?",
                "opcoes": ["Índia", "China", "EUA", "Indonésia"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital do Japão?",
                "opcoes": ["Kyoto", "Tóquio", "Osaka", "Nagoya"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o vulcão Vesúvio localizado?",
                "opcoes": ["Itália", "Japão", "Havaí", "Islândia"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o estreito de Gibraltar?",
                "opcoes": ["Atlântico-Mediterrâneo", "Pacífico-Atlântico", "Índico-Pacífico", "Ártico-Atlântico"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital da Argentina?",
                "opcoes": ["Buenos Aires", "Santiago", "Lima", "Montevidéu"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o maior lago do mundo?",
                "opcoes": ["Baikal", "Superior", "Cáspio", "Vitória"],
                "resposta_correta": 2,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país com forma de bota?",
                "opcoes": ["Espanha", "Itália", "Grécia", "Portugal"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital da África do Sul?",
                "opcoes": ["Joanesburgo", "Cidade do Cabo", "Pretória", "Durban"],
                "resposta_correta": 2,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o meridiano principal?",
                "opcoes": ["Equador", "Greenwich", "Trópico de Câncer", "Trópico de Capricórnio"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o oceano entre Europa e América?",
                "opcoes": ["Pacífico", "Atlântico", "Índico", "Ártico"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital do México?",
                "opcoes": ["Cidade do México", "Guadalajara", "Monterrey", "Cancún"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país mais ao norte?",
                "opcoes": ["Noruega", "Rússia", "Canadá", "Groenlândia (Dinamarca)"],
                "resposta_correta": 3,
                "categoria": "geografia"
            }
        ],
        "hard": [
            {
                "pergunta": "Qual é a capital de Liechtenstein?",
                "opcoes": ["Vaduz", "Berna", "Viena", "Luxemburgo"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país com mais fronteiras?",
                "opcoes": ["Rússia", "China", "Brasil", "Alemanha"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o lago mais profundo?",
                "opcoes": ["Cáspio", "Baikal", "Titicaca", "Superior"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a maior península?",
                "opcoes": ["Ibérica", "Arábica", "Indochina", "Escandinava"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital de Myanmar?",
                "opcoes": ["Yangon", "Naypyidaw", "Mandalay", "Bangkok"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o rio mais volumoso?",
                "opcoes": ["Nilo", "Amazonas", "Mississipi", "Congo"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país enclavado na África do Sul?",
                "opcoes": ["Lesoto", "Suazilândia", "Botsuana", "Namíbia"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital de Fiji?",
                "opcoes": ["Nadi", "Suva", "Lautoka", "Labasa"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o maior arquipélago?",
                "opcoes": ["Filipinas", "Indonésia", "Japão", "Maldivas"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a linha imaginária que divide norte e sul?",
                "opcoes": ["Equador", "Meridiano de Greenwich", "Trópico de Câncer", "Círculo Polar"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital de Burkina Faso?",
                "opcoes": ["Ouagadougou", "Bobo-Dioulasso", "Koudougou", "Banfora"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país com mais vulcões?",
                "opcoes": ["Japão", "Indonésia", "Islândia", "Itália"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital de Quirguistão?",
                "opcoes": ["Bishkek", "Osh", "Jalal-Abad", "Karakol"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o maior canyon?",
                "opcoes": ["Grand Canyon", "Fish River", "Yarlung Tsangpo", "Colca"],
                "resposta_correta": 2,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital de Palau?",
                "opcoes": ["Koror", "Ngerulmud", "Melekeok", "Airai"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país transcontinental entre Ásia e Europa?",
                "opcoes": ["Turquia", "Todas", "Rússia", "Cazaquistão"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a ilha mais populosa?",
                "opcoes": ["Java", "Honshu", "Luzon", "Sumatra"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é a capital de Timor-Leste?",
                "opcoes": ["Baucau", "Díli", "Maliana", "Ermera"],
                "resposta_correta": 1,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o rio que forma o Grand Canyon?",
                "opcoes": ["Colorado", "Mississippi", "Missouri", "Rio Grande"],
                "resposta_correta": 0,
                "categoria": "geografia"
            },
            {
                "pergunta": "Qual é o país com mais lagos?",
                "opcoes": ["Canadá", "Finlândia", "Rússia", "EUA"],
                "resposta_correta": 0,
                "categoria": "geografia"
            }
        ]
    },
    "historia": {
        "easy": [
                {
                    "pergunta": "Quem descobriu o Brasil?",
                    "opcoes": ["Cabral", "Colombo", "Vasco da Gama", "Magalhães"],
                    "resposta_correta": 0,
                    "categoria": "historia"
                },
            {
                    "pergunta": "Qual foi a guerra entre 1939-1945?",
                    "opcoes": ["I Guerra Mundial", "II Guerra Mundial", "Guerra Fria", "Vietnam"],
                    "resposta_correta": 1,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Quem foi o primeiro presidente do Brasil?",
                    "opcoes": ["Getúlio Vargas", "Deodoro da Fonseca", "Juscelino Kubitschek", "Lula"],
                    "resposta_correta": 1,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Quando foi a Independência do Brasil?",
                    "opcoes": ["1822", "1500", "1889", "1960"],
                    "resposta_correta": 0,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Quem pintou a Mona Lisa?",
                    "opcoes": ["Van Gogh", "Da Vinci", "Picasso", "Michelangelo"],
                    "resposta_correta": 1,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Qual império caiu em 1453?",
                    "opcoes": ["Romano", "Bizantino", "Otomano", "Mongol"],
                    "resposta_correta": 1,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Quem foi Cleópatra?",
                    "opcoes": ["Rainha do Egito", "Rainha da Inglaterra", "Imperatriz romana", "Deusa grega"],
                    "resposta_correta": 0,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Quando começou a Revolução Francesa?",
                    "opcoes": ["1789", "1776", "1812", "1917"],
                    "resposta_correta": 0,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Quem foi Napoleão?",
                    "opcoes": ["Rei francês", "Imperador francês", "General inglês", "Czar russo"],
                    "resposta_correta": 1,
                    "categoria": "historia"
                    },
            {
                    "pergunta": "Qual foi a primeira civilização?",
                    "opcoes": ["Egípcia", "Mesopotâmica", "Grega", "Romana"],
                    "resposta_correta": 1,
                    "categoria": "historia"
                    }
        ],
        "medium": [
            {
                "pergunta": "Qual foi a causa da I Guerra Mundial?",
                "opcoes": ["Assassinato de Franz Ferdinand", "Revolução Russa", "Independência EUA", "Queda da Bastilha"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi o líder da Revolução Russa?",
                "opcoes": ["Stalin", "Lênin", "Trotsky", "Gorbachev"],
                "resposta_correta": 1,
                "categoria": "historia"
            },
            {
                "pergunta": "Quando foi a Queda do Muro de Berlim?",
                "opcoes": ["1989", "1991", "1945", "1961"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual tratado encerrou a I Guerra?",
                "opcoes": ["Versalhes", "Tordesilhas", "Westfália", "Utrecht"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem descobriu a América?",
                "opcoes": ["Cabral", "Colombo", "Vespucci", "Cook"],
                "resposta_correta": 1,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi o período da Idade das Trevas?",
                "opcoes": ["Idade Antiga", "Idade Média", "Renascimento", "Iluminismo"],
                "resposta_correta": 1,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi Martinho Lutero?",
                "opcoes": ["Reformador", "Explorador", "Rei", "Pintor"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quando foi a Revolução Industrial?",
                "opcoes": ["Século XVIII", "Século XVII", "Século XIX", "Século XX"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual império conquistou Constantinopla?",
                "opcoes": ["Otomano", "Persa", "Mongol", "Romano"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi o primeiro homem na Lua?",
                "opcoes": ["Gagarin", "Armstrong", "Aldrin", "Collins"],
                "resposta_correta": 1,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi a guerra de 1812?",
                "opcoes": ["Napoleônica", "EUA vs Inglaterra", "Civil Americana", "Franco-Prussiana"],
                "resposta_correta": 1,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem assinou a Magna Carta?",
                "opcoes": ["João Sem Terra", "Henrique VIII", "Guilherme o Conquistador", "Ricardo Coração de Leão"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quando foi o Holocausto?",
                "opcoes": ["II Guerra", "I Guerra", "Guerra Fria", "Vietnam"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi Gengis Khan?",
                "opcoes": ["Líder mongol", "Imperador chinês", "Rei persa", "Sultão otomano"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi o tratado após II Guerra?",
                "opcoes": ["Potsdam", "Versalhes", "Tordesilhas", "Yalta"],
                "resposta_correta": 3,
                "categoria": "historia"
            }
        ],
        "hard": [
            {
                "pergunta": "Qual foi a Batalha de Waterloo?",
                "opcoes": ["Napoleão derrotado", "Vitória francesa", "Independência", "Revolução"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi o faraó Tutankhamon?",
                "opcoes": ["Egípcio", "Assírio", "Hitita", "Sumério"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quando foi a Guerra dos Cem Anos?",
                "opcoes": ["1337-1453", "1618-1648", "1914-1918", "1939-1945"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi o Código de Hamurabi?",
                "opcoes": ["Leis babilônicas", "Tratado persa", "Lei romana", "Código grego"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi Sun Tzu?",
                "opcoes": ["General chinês", "Filósofo grego", "Rei egípcio", "Imperador romano"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi a Peste Negra?",
                "opcoes": ["Bubônica", "Cólera", "Varíola", "Gripe"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quando foi a Queda de Roma?",
                "opcoes": ["476 d.C.", "1453 d.C.", "330 d.C.", "1054 d.C."],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi o líder da Independência Indiana?",
                "opcoes": ["Gandhi", "Nehru", "Jinnah", "Bose"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi o Tratado de Tordesilhas?",
                "opcoes": ["Espanha-Portugal", "Inglaterra-França", "Alemanha-Rússia", "EUA-México"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi o czar Ivan o Terrível?",
                "opcoes": ["Russo", "Polonês", "Sueco", "Otomano"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi a Revolução Gloriosa?",
                "opcoes": ["Inglaterra 1688", "França 1789", "EUA 1776", "Rússia 1917"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem descobriu a penicilina?",
                "opcoes": ["Fleming", "Pasteur", "Koch", "Jenner"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quando foi o Tratado de Westfália?",
                "opcoes": ["1648", "1815", "1919", "1945"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi a Dinastia Ming?",
                "opcoes": ["Chinesa", "Japonesa", "Coreana", "Mongol"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi o rei Sol?",
                "opcoes": ["Luís XIV", "Carlos V", "Henrique IV", "Filipe II"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi a Guerra das Rosas?",
                "opcoes": ["Inglaterra", "França", "Espanha", "Alemanha"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi Marco Pólo?",
                "opcoes": ["Explorador italiano", "Navegador português", "Conquistador espanhol", "Rei francês"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quando foi o Renascimento Harlem?",
                "opcoes": ["1920s", "1800s", "1500s", "1700s"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Qual foi o Império Asteca conquistado por?",
                "opcoes": ["Cortes", "Pizarro", "Cabral", "Drake"],
                "resposta_correta": 0,
                "categoria": "historia"
            },
            {
                "pergunta": "Quem foi o filósofo Confúcio?",
                "opcoes": ["Chinês", "Indiano", "Grego", "Persa"],
                "resposta_correta": 0,
                "categoria": "historia"
            }
        ]
    },
    "ti": {
        "easy": [
            {
                "pergunta": "O que é CPU?",
                "opcoes": ["Unidade Central de Processamento", "Memória RAM", "Disco Rígido", "Monitor"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o navegador Google?",
                "opcoes": ["Firefox", "Chrome", "Edge", "Safari"],
                "resposta_correta": 1,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é Wi-Fi?",
                "opcoes": ["Rede sem fio", "Cabo", "Bluetooth", "Ethernet"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o sistema Android?",
                "opcoes": ["iOS", "Windows", "Linux", "Móvel Google"],
                "resposta_correta": 3,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é e-mail?",
                "opcoes": ["Correio eletrônico", "Mensagem texto", "Chamada vídeo", "Rede social"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o fundador da Microsoft?",
                "opcoes": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"],
                "resposta_correta": 1,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é USB?",
                "opcoes": ["Conector universal", "Teclado", "Mouse", "Impressora"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o site de vídeos?",
                "opcoes": ["Facebook", "YouTube", "Instagram", "Twitter"],
                "resposta_correta": 1,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é firewall?",
                "opcoes": ["Proteção rede", "Antivírus", "Backup", "Update"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o símbolo @ usado em?",
                "opcoes": ["E-mail", "Hashtag", "URL", "Password"],
                "resposta_correta": 0,
                "categoria": "ti"
            }
        ],
        "medium": [
            {
                "pergunta": "O que é HTML?",
                "opcoes": ["Linguagem marcação", "Banco dados", "Sistema operacional", "Protocolo rede"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o protocolo internet?",
                "opcoes": ["HTTP", "FTP", "SMTP", "TCP/IP"],
                "resposta_correta": 3,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é SQL?",
                "opcoes": ["Linguagem consulta", "Programação", "Rede", "Segurança"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o cloud computing?",
                "opcoes": ["Armazenamento online", "Hardware local", "Software desktop", "Rede local"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é VPN?",
                "opcoes": ["Rede privada virtual", "Vírus", "Firewall", "Backup"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o fundador do Facebook?",
                "opcoes": ["Bill Gates", "Mark Zuckerberg", "Elon Musk", "Jeff Bezos"],
                "resposta_correta": 1,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é Big Data?",
                "opcoes": ["Grandes volumes dados", "Pequenos arquivos", "Programas simples", "Redes pequenas"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o AI?",
                "opcoes": ["Inteligência artificial", "Interface usuário", "Banco dados", "Sistema operacional"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é blockchain?",
                "opcoes": ["Tecnologia criptomoeda", "Navegador", "Antivírus", "Editor texto"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o IPv4?",
                "opcoes": ["Endereço internet", "Protocolo email", "Linguagem programação", "Hardware"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é API?",
                "opcoes": ["Interface programação", "Sistema arquivo", "Rede social", "Banco dados"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o Linux?",
                "opcoes": ["Sistema operacional open source", "Windows alternativo", "Mac OS", "iOS"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é phishing?",
                "opcoes": ["Ataque cibernético", "Programa", "Rede", "Hardware"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o HTTP status 404?",
                "opcoes": ["Não encontrado", "OK", "Redirecionado", "Erro servidor"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é IoT?",
                "opcoes": ["Internet das coisas", "Inteligência operacional", "Interface técnica", "Informação online"],
                "resposta_correta": 0,
                "categoria": "ti"
            }
        ],
        "hard": [
            {
                "pergunta": "Qual é o algoritmo de busca Google?",
                "opcoes": ["PageRank", "Dijkstra", "Bubble Sort", "Quick Sort"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o protocolo seguro?",
                "opcoes": ["HTTPS", "HTTP", "FTP", "SMTP"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é machine learning?",
                "opcoes": ["Aprendizado máquina", "Programação manual", "Banco dados", "Rede neural"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o Bitcoin baseado em?",
                "opcoes": ["Blockchain", "Cloud", "AI", "Big Data"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é quantum computing?",
                "opcoes": ["Computação quântica", "Clássica", "Paralela", "Distribuída"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o OSI model camadas?",
                "opcoes": ["7", "5", "4", "6"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é ransomware?",
                "opcoes": ["Malware resgate", "Vírus simples", "Spyware", "Adware"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o IPv6 tamanho?",
                "opcoes": ["128 bits", "32 bits", "64 bits", "16 bits"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é DevOps?",
                "opcoes": ["Desenvolvimento operações", "Design ops", "Data ops", "Dev tools"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o framework JavaScript?",
                "opcoes": ["React", "Java", "C++", "Python"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é containerização?",
                "opcoes": ["Docker", "Todas", "Virtualização", "Cloud"],
                "resposta_correta": 1,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o GDPR?",
                "opcoes": ["Regulamento dados UE", "Protocolo rede", "Linguagem", "Hardware"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é edge computing?",
                "opcoes": ["Computação borda", "Central", "Cloud", "Mainframe"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o 5G?",
                "opcoes": ["Quinta geração móvel", "Quarta", "Sexta", "Terceira"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é cybersecurity?",
                "opcoes": ["Segurança cibernética", "Programação", "Design", "Análise"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o algoritmo criptografia AES?",
                "opcoes": ["Simétrico", "Assimétrico", "Hash", "Nenhum"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é NoSQL?",
                "opcoes": ["Banco não relacional", "Relacional", "SQL", "Oracle"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o Kubernetes?",
                "opcoes": ["Orquestração containers", "Banco dados", "Linguagem", "OS"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "O que é microservices?",
                "opcoes": ["Arquitetura distribuída", "Monolítica", "Centralizada", "Legado"],
                "resposta_correta": 0,
                "categoria": "ti"
            },
            {
                "pergunta": "Qual é o Scrum?",
                "opcoes": ["Metodologia ágil", "Waterfall", "Kanban", "Lean"],
                "resposta_correta": 0,
                "categoria": "ti"
            }
        ]
    },
    "gerais": {
        "easy": [
            {
                "pergunta": "Qual é a capital do Brasil?",
                "opcoes": ["Rio", "Brasília", "SP", "Belo Horizonte"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quem escreveu Harry Potter?",
                "opcoes": ["Tolkien", "Rowling", "Lewis", "Martin"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o planeta mais próximo do Sol?",
                "opcoes": ["Terra", "Mercúrio", "Vênus", "Marte"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quanto é 10 + 10?",
                "opcoes": ["10", "20", "30", "0"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o animal que mia?",
                "opcoes": ["Cão", "Gato", "Pássaro", "Peixe"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a cor do céu?",
                "opcoes": ["Verde", "Azul", "Vermelho", "Amarelo"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quantos dias tem uma semana?",
                "opcoes": ["5", "7", "10", "30"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o oposto de quente?",
                "opcoes": ["Frio", "Morno", "Quente", "Fervente"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o instrumento para ver estrelas?",
                "opcoes": ["Microscópio", "Telescópio", "Binóculo", "Lupa"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o mês do Natal?",
                "opcoes": ["Janeiro", "Dezembro", "Julho", "Abril"],
                "resposta_correta": 1,
                "categoria": "gerais"
            }
        ],
        "medium": [
            {
                "pergunta": "Qual é o maior planeta do sistema solar?",
                "opcoes": ["Terra", "Júpiter", "Saturno", "Netuno"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quem descobriu a gravidade?",
                "opcoes": ["Einstein", "Newton", "Galileo", "Hawking"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a moeda do Japão?",
                "opcoes": ["Dólar", "Iene", "Euro", "Libra"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o autor de \"1984\"?",
                "opcoes": ["Huxley", "Orwell", "Bradbury", "Asimov"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o elemento químico Au?",
                "opcoes": ["Prata", "Ouro", "Ferro", "Cobre"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a capital da Austrália?",
                "opcoes": ["Sydney", "Canberra", "Melbourne", "Perth"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o número pi?",
                "opcoes": ["3.14", "2.71", "1.61", "9.81"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quem pintou a Capela Sistina?",
                "opcoes": ["Da Vinci", "Michelangelo", "Rafael", "Botticelli"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o oceano mais profundo?",
                "opcoes": ["Atlântico", "Pacífico", "Índico", "Ártico"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a fórmula da água?",
                "opcoes": ["H2O", "CO2", "NaCl", "O2"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o país com mais idiomas?",
                "opcoes": ["Índia", "Papua Nova Guiné", "Indonésia", "Brasil"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o livro mais vendido?",
                "opcoes": ["Bíblia", "Harry Potter", "Senhor dos Anéis", "Dom Quixote"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o animal mais rápido?",
                "opcoes": ["Leão", "Guepardo", "Cavalo", "Falcão"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a montanha mais alta?",
                "opcoes": ["K2", "Everest", "Kilimanjaro", "Aconcágua"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o rio mais longo?",
                "opcoes": ["Nilo", "Amazonas", "Yangtzé", "Mississipi"],
                "resposta_correta": 1,
                "categoria": "gerais"
            }
        ],
        "hard": [
            {
                "pergunta": "Qual é o nome científico do homem?",
                "opcoes": ["Homo sapiens", "Homo erectus", "Homo habilis", "Homo neanderthalensis"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a constante de Avogadro?",
                "opcoes": ["6.022 x 10^23", "3 x 10^8", "9.81", "6.626 x 10^-34"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quem inventou o telefone?",
                "opcoes": ["Edison", "Bell", "Tesla", "Marconi"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o país com mais Patrimônios UNESCO?",
                "opcoes": ["Itália", "China", "Espanha", "França"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o elemento mais abundante no universo?",
                "opcoes": ["Hidrogênio", "Hélio", "Oxigênio", "Carbono"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a capital de Malta?",
                "opcoes": ["Valletta", "Mdina", "Victoria", "Sliema"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o teorema de Fermat último?",
                "opcoes": ["Sem solução para n>2", "a^n + b^n = c^n", "Ambas", "Nenhuma"],
                "resposta_correta": 2,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quem foi o primeiro Nobel de Literatura?",
                "opcoes": ["Kipling", "Prudhomme", "Shaw", "Mann"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o lago mais alto?",
                "opcoes": ["Titicaca", "Baikal", "Cáspio", "Superior"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o compositor de \"Quatro Estações\"?",
                "opcoes": ["Bach", "Vivaldi", "Mozart", "Beethoven"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a distância Terra-Sol?",
                "opcoes": ["150 milhões km", "1 bilhão km", "1 milhão km", "300 milhões km"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o animal com mais dentes?",
                "opcoes": ["Elefante", "Tubarão", "Crocodilo", "Caracol"],
                "resposta_correta": 3,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o país com mais fusos horários?",
                "opcoes": ["Rússia", "EUA", "China", "França"],
                "resposta_correta": 3,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o livro \"Guerra e Paz\"?",
                "opcoes": ["Tolstói", "Dostoiévski", "Pushkin", "Gogol"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o elemento 79 tabela periódica?",
                "opcoes": ["Ouro", "Prata", "Platina", "Mercúrio"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a capital de Liechtenstein?",
                "opcoes": ["Vaduz", "Schaan", "Triesen", "Balzers"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é a teoria do Big Bang?",
                "opcoes": ["Origem universo", "Evolução", "Relatividade", "Quantum"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Quem foi o inventor do avião?",
                "opcoes": ["Santos Dumont", "Irmãos Wright", "Lilienthal", "Cayley"],
                "resposta_correta": 1,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o rio com mais afluentes?",
                "opcoes": ["Amazonas", "Nilo", "Mississipi", "Ganges"],
                "resposta_correta": 0,
                "categoria": "gerais"
            },
            {
                "pergunta": "Qual é o pintor de \"Noite Estrelada\"?",
                "opcoes": ["Van Gogh", "Monet", "Renoir", "Degas"],
                "resposta_correta": 0,
                "categoria": "gerais"
            }
        ]
    }
}

QTD_POR_DIFICULDADE = {"easy": 10, "medium": 15, "hard": 20}


def obter_perguntas(categoria: str = "geral", dificuldade: str = "easy", quantidade: int = 10) -> List[Pergunta]:
    """
    Retorna uma lista de perguntas baseada na categoria e dificuldade especificadas

    Args:
        categoria: Categoria das perguntas (geral, humanas, exatas, biologicas, geografia, historia, ti)
        dificuldade: Nível de dificuldade (easy, medium, hard)
        quantidade: Número de perguntas desejadas

    Returns:
        Lista de objetos Pergunta
    """
    # Garantir categoria existente
    if categoria not in PERGUNTAS_DB:
        categoria = "geral"

    # Garantir dificuldade existente
    if dificuldade not in PERGUNTAS_DB[categoria]:
        dificuldade = "easy"

    perguntas_disponiveis = PERGUNTAS_DB[categoria][dificuldade].copy()
    quantidade = QTD_POR_DIFICULDADE[dificuldade]

    # Evita repetição (usa sample limitado ao tamanho máximo possível)
    if len(perguntas_disponiveis) == 0:
        print(
            f"Aviso: Nenhuma pergunta disponível para {categoria}/{dificuldade}")
        return []

    if len(perguntas_disponiveis) < quantidade:
        print(
            f"Aviso: Apenas {len(perguntas_disponiveis)} perguntas disponíveis para {categoria}/{dificuldade}")
        quantidade = len(perguntas_disponiveis)

    perguntas_selecionadas = random.sample(perguntas_disponiveis, quantidade)

    perguntas_objetos = []


    for i, p in enumerate(perguntas_selecionadas):
        opcoes = p["opcoes"].copy()
        correta = p["resposta_correta"]

        opcoes_tuplas = [(op, idx == correta) for idx, op in enumerate(opcoes)]

        random.shuffle(opcoes_tuplas)

        opcoes_embaralhadas = [op for op, _ in opcoes_tuplas]
        novo_indice_correto = next(
            idx for idx, (_, correta) in enumerate(opcoes_tuplas) if correta)

        perguntas_objetos.append(Pergunta(
            id=i + 1,
            pergunta=p["pergunta"],
            opcoes=opcoes_embaralhadas,
            resposta_correta=novo_indice_correto,
            categoria=p["categoria"]
        ))
        
    return perguntas_objetos


def obter_categorias_disponiveis() -> List[str]:
    """Retorna lista de categorias disponíveis"""
    return list(PERGUNTAS_DB.keys())


def obter_dificuldades_disponiveis(categoria: str = "geral") -> List[str]:
    """Retorna lista de dificuldades disponíveis para uma categoria"""
    if categoria in PERGUNTAS_DB:
        return list(PERGUNTAS_DB[categoria].keys())
    return list(QTD_POR_DIFICULDADE.keys())


def obter_estatisticas_perguntas() -> Dict[str, Any]:
    """Retorna estatísticas sobre as perguntas disponíveis"""
    total_perguntas = 0
    categorias_info = {}

    for categoria, dificuldades in PERGUNTAS_DB.items():
        categoria_total = 0
        dificuldades_info = {}

        for dificuldade, perguntas in dificuldades.items():
            quantidade = len(perguntas)
            categoria_total += quantidade
            dificuldades_info[dificuldade] = quantidade

        categorias_info[categoria] = {
            "total": categoria_total,
            "dificuldades": dificuldades_info
        }
        total_perguntas += categoria_total

    return {
        "total_perguntas": total_perguntas,
        "categorias": categorias_info
    }
