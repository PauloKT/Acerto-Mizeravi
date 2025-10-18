// login.js
(function(){
  const btn = document.getElementById('btnLogin');
  if(!btn) return;

  if(window.createShootingStars) window.createShootingStars();

  btn.addEventListener('click', (e)=>{
    e.preventDefault();
    const emailOrLogin = document.getElementById('email').value.trim();
    const pwd = document.getElementById('pwd').value.trim();
    if(!emailOrLogin || !pwd){ alert('Preencha todos os campos'); return; }

    const raw = localStorage.getItem('tabareli_users');
    const users = raw ? JSON.parse(raw) : [];
    const user = users.find(u => u.login === emailOrLogin || u.email === emailOrLogin);
    if(user && user.password === pwd){
      localStorage.setItem('tabareli_current', user.login);
      try{ new Audio('assets/click.mp3').play().catch(()=>{}); }catch(e){}
      window.location.href = 'menu.html';
    } else {
      alert('Usuário ou senha incorretos.');
    }
  });
})();
