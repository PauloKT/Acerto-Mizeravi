(function(){
  const btnStart = document.getElementById('btnStart');
  if(!btnStart) return;

  const click = new Audio('sound/click.mp3'); 
  click.volume = 0.5; 
  click.preload = 'auto';

  const cur = localStorage.getItem('tabareli_current');
  if(!cur){ window.location.href = 'login.html'; return; }

  // Buscar dados do usuário no localStorage
  const userDataRaw = localStorage.getItem('tabareli_user_data');
  const userData = userDataRaw ? JSON.parse(userDataRaw) : null;
  
  const welcome = document.getElementById('welcomeText');
  if(welcome) {
    welcome.textContent = userData ? `Bem-vindo, ${userData.nome}` : 'Bem-vindo!';
  }

  // Garantir que o áudio global esteja tocando
  if (window.AudioManager) {
    window.AudioManager.play();
  }

  btnStart.addEventListener('click', ()=>{ 
    click.currentTime=0; 
    click.play().catch(()=>{}); 
    window.location.href='modes.html'; 
  });
  
  document.getElementById('btnRanking').addEventListener('click', ()=>{ 
    click.currentTime=0; 
    click.play().catch(()=>{}); 
    window.location.href='ranking.html'; 
  });
  
  document.getElementById('btnLogout').addEventListener('click', ()=>{ 
    click.currentTime=0; 
    click.play().catch(()=>{}); 
    localStorage.removeItem('tabareli_current');
    localStorage.removeItem('tabareli_user_data');
    window.location.href='login.html'; 
  });

  if(window.createShootingStars) window.createShootingStars();
})();
