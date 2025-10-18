// gameover.js
(function(){
  const el = document.getElementById('finalScore');
  if(!el) return;
  const s = localStorage.getItem('lastScore') || 0;
  el.textContent = s;
  try{ new Audio('assets/gameover.mp3').play().catch(()=>{}); }catch(e){}
  window.restartGame = function(){ try{ new Audio('assets/click.mp3').play().catch(()=>{}); }catch(e){}; window.location.href='modes.html'; };
  window.viewRanking = function(){ try{ new Audio('assets/click.mp3').play().catch(()=>{}); }catch(e){}; window.location.href='ranking.html'; };
  window.goHome = function(){ try{ new Audio('assets/click.mp3').play().catch(()=>{}); }catch(e){}; window.location.href='menu.html'; };
})();
