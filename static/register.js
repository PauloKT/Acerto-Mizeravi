// register.js - Sistema de registro usando endpoints da API
(function(){
  const form = document.getElementById('registerForm');
  if(!form) return;
  
  form.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const nome = document.getElementById('name_input').value.trim();
    const email = document.getElementById('email_input').value.trim();
    const login = document.getElementById('login_reg_input').value.trim();
    const senha = document.getElementById('password_reg_input').value;
    
    if(!nome || !email || !login || !senha){ 
      alert('Preencha todos os campos'); 
      return; 
    }

    try {
      // Registrar usuário via API
      const response = await fetch('/api/registrar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          nome: nome,
          email: email,
          login: login,
          senha: senha
        })
      });

      const data = await response.json();

      if(data.sucesso) {
        alert('Conta criada com sucesso! Faça login.');
        window.location.href = 'login.html';
      } else {
        if(data.erros && data.erros.length > 0) {
          alert('Erros encontrados:\n' + data.erros.join('\n'));
        } else {
          alert(data.erro || 'Erro ao criar conta');
        }
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
      alert('Erro de conexão. Tente novamente.');
    }
  });
})();