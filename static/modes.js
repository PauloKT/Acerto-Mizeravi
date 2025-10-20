// modes.js
(function(){
  const btns = document.querySelectorAll('.mode-btn');
  if(!btns.length) return;
  const click = new Audio('sound/click.mp3'); click.preload = 'auto'; click.volume = 0.5;
  btns.forEach(b=>{
    b.addEventListener('click', ()=>{
      click.currentTime=0; click.play().catch(()=>{});
      const mode = b.dataset.mode;
      localStorage.setItem('tabareli_chosen_mode', mode);
      window.location.href = 'game.html';
    });
  });
})();
