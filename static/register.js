(function(){
  const form = document.getElementById('registerForm');
  if(!form) return;
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const name = document.getElementById('name_input').value.trim();
    const email = document.getElementById('email_input').value.trim();
    const login = document.getElementById('login_reg_input').value.trim();
    const pass = document.getElementById('password_reg_input').value;
    if(!name||!email||!login||!pass){ alert('Preencha todos os campos'); return; }

    const raw = localStorage.getItem('tabareli_users');
    const users = raw ? JSON.parse(raw) : [];

    if(users.some(u=>u.login===login || u.email===email)){ alert('Login ou e-mail já cadastrado.'); return; }

    users.push({ name, email, login, password: pass });
    localStorage.setItem('tabareli_users', JSON.stringify(users));
    alert('Conta criada com sucesso! Faça login.');
    window.location.href = 'login.html';
  });
})();