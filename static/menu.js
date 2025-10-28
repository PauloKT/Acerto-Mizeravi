// menu.js - Sistema de menu usando endpoints da API
(function(){
  const intro = new Audio('sound/intro.mp3'); 
  intro.loop = true; 
  intro.volume = 0.2; 
  intro.preload = 'auto';
  
  const click = new Audio('sound/click.mp3'); 
  click.volume = 0.5; 
  click.preload = 'auto';

  // Verificar se há usuário logado
  const usuarioAtual = sessionStorage.getItem('usuario_atual');
  if(!usuarioAtual){ 
    window.location.href = 'login.html'; 
    return; 
  }

  try {
    const usuario = JSON.parse(usuarioAtual);
    const welcome = document.getElementById('welcomeText');
    if(welcome) welcome.textContent = `Bem-vindo, ${usuario.nome}`;
  } catch (e) {
    console.error('Erro ao parsear dados do usuário:', e);
    window.location.href = 'login.html';
    return;
  }

  function tryPlay(){ 
    try{ 
      intro.currentTime=0; 
      intro.play().catch(()=>{}); 
    }catch(e){}
    document.removeEventListener('click', tryPlay);
    document.removeEventListener('touchstart', tryPlay);
    document.removeEventListener('keydown', tryPlay);
  }
  
  document.addEventListener('click', tryPlay, { once:true });
  document.addEventListener('touchstart', tryPlay, { once:true });
  document.addEventListener('keydown', tryPlay, { once:true });

  document.getElementById('btnQuiz').addEventListener('click', ()=>{ 
    click.currentTime=0; 
    click.play().catch(()=>{}); 
    window.location.href='quiz.html'; 
  });
  
  document.getElementById('btnRanking').addEventListener('click', ()=>{ 
    click.currentTime=0; 
    click.play().catch(()=>{}); 
    window.location.href='ranking.html'; 
  });
  
  document.getElementById('btnLogout').addEventListener('click', ()=>{ 
    click.currentTime=0; 
    click.play().catch(()=>{}); 
    sessionStorage.removeItem('usuario_atual'); 
    window.location.href='login.html'; 
  });

  if(window.createShootingStars) window.createShootingStars();
})();
