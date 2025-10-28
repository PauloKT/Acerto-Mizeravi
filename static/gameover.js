// gameover.js - Sistema de game over usando endpoints da API
(function(){
  const el = document.getElementById('finalScore');
  if(!el) return;

  // Verificar se há usuário logado
  const usuarioAtual = sessionStorage.getItem('usuario_atual');
  if(!usuarioAtual){ 
    window.location.href = 'login.html'; 
    return; 
  }

  // Obter pontuação da sessão atual
  const pontuacao = sessionStorage.getItem('pontuacao_final') || 0;
  el.textContent = pontuacao;

  // Tocar som de game over
  try{ 
    new Audio('sound/gameover.mp3').play().catch(()=>{}); 
  }catch(e){}

  // Funções de navegação
  window.restartGame = function(){ 
    try{ 
      new Audio('sound/click.mp3').play().catch(()=>{}); 
    }catch(e){}; 
    window.location.href='quiz.html'; 
  };
  
  window.viewRanking = function(){ 
    try{ 
      new Audio('sound/click.mp3').play().catch(()=>{}); 
    }catch(e){}; 
    window.location.href='ranking.html'; 
  };
  
  window.goHome = function(){ 
    try{ 
      new Audio('sound/click.mp3').play().catch(()=>{}); 
    }catch(e){}; 
    window.location.href='menu.html'; 
  };
})();
