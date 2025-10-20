(function(){
  const btnStart = document.getElementById('btnStart');
  if(!btnStart) return;

  const intro = new Audio('sound/intro.mp3'); intro.volume = 0.2; intro.preload = 'auto';
  const click = new Audio('sound/click.mp3'); click.volume = 0.5; click.preload = 'auto';

  const cur = localStorage.getItem('tabareli_current');
  if(!cur){ window.location.href = 'login.html'; return; }

  const usersRaw = localStorage.getItem('tabareli_users'); const users = usersRaw?JSON.parse(usersRaw):[];
  const u = users.find(x=>x.login===cur || x.email===cur);
  const welcome = document.getElementById('welcomeText');
  if(welcome) welcome.textContent = u ? `Bem-vindo, ${u.name}` : 'Bem-vindo!';

  function tryPlay(){ try{ intro.currentTime=0; intro.play().catch(()=>{}); }catch(e){}
    document.removeEventListener('click', tryPlay);
    document.removeEventListener('touchstart', tryPlay);
    document.removeEventListener('keydown', tryPlay);
  }
  document.addEventListener('click', tryPlay, { once:true });
  document.addEventListener('touchstart', tryPlay, { once:true });
  document.addEventListener('keydown', tryPlay, { once:true });

  btnStart.addEventListener('click', ()=>{ click.currentTime=0; click.play().catch(()=>{}); window.location.href='modes.html'; });
  document.getElementById('btnQuiz').addEventListener('click', ()=>{ click.currentTime=0; click.play().catch(()=>{}); window.location.href='quiz.html'; });
  document.getElementById('btnRanking').addEventListener('click', ()=>{ click.currentTime=0; click.play().catch(()=>{}); window.location.href='ranking.html'; });
  document.getElementById('btnLogout').addEventListener('click', ()=>{ click.currentTime=0; click.play().catch(()=>{}); localStorage.removeItem('tabareli_current'); window.location.href='login.html'; });

  if(window.createShootingStars) window.createShootingStars();
})();
