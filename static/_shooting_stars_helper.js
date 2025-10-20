// Shooting Stars Helper
// Cria estrelas cadentes animadas para o fundo do jogo

function createShootingStars() {
    const container = document.querySelector('.shooting-container');
    if (!container) return;

    function createShootingStar() {
        const star = document.createElement('div');
        star.style.cssText = `
            position: absolute;
            width: 2px;
            height: 2px;
            background: linear-gradient(45deg, #fff, #5ef2ff);
            border-radius: 50%;
            box-shadow: 0 0 6px #5ef2ff;
            top: ${Math.random() * 50}%;
            left: ${Math.random() * 100}%;
            animation: shootingStar 2s linear forwards;
            z-index: 1;
        `;

        // Adicionar trail
        const trail = document.createElement('div');
        trail.style.cssText = `
            position: absolute;
            width: 100px;
            height: 1px;
            background: linear-gradient(90deg, transparent, #5ef2ff, transparent);
            top: 50%;
            left: -100px;
            transform: translateY(-50%);
            animation: shootingTrail 2s linear forwards;
        `;

        star.appendChild(trail);
        container.appendChild(star);

        // Remover após animação
        setTimeout(() => {
            if (star.parentNode) {
                star.parentNode.removeChild(star);
            }
        }, 2000);
    }

    // Criar estrelas periodicamente
    setInterval(createShootingStar, 3000 + Math.random() * 2000);
}

// Adicionar CSS para animações
const style = document.createElement('style');
style.textContent = `
    @keyframes shootingStar {
        0% {
            transform: translateX(0) translateY(0);
            opacity: 1;
        }
        100% {
            transform: translateX(200px) translateY(100px);
            opacity: 0;
        }
    }
    
    @keyframes shootingTrail {
        0% {
            transform: translateY(-50%) scaleX(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        100% {
            transform: translateY(-50%) scaleX(1);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Exportar função globalmente
window.createShootingStars = createShootingStars;
