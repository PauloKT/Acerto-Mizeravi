(function(){
  const form = document.getElementById('registerForm');
  if(!form) return;
  
  form.addEventListener('submit', async (e)=>{
    e.preventDefault();
    
    const email = document.getElementById('email_input').value.trim();
    const login = document.getElementById('login_reg_input').value.trim();
    const pass = document.getElementById('password_reg_input').value;
    
    if(!email||!login||!pass){ 
      alert('Preencha todos os campos'); 
      return; 
    }

    try {
      const response = await fetch('/api/registrar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          nome: login, // Usar o login como nome
          email: email
        })
      });

      const data = await response.json();

      if (data.sucesso) {
        alert('Conta criada com sucesso! Faça login.');
        window.location.href = 'login.html';
      } else {
        if (data.erros) {
          alert('Erros: ' + data.erros.join(', '));
        } else {
          alert('Erro: ' + data.erro);
        }
      }
    } catch (error) {
      console.error('Erro ao registrar:', error);
      alert('Erro ao conectar com o servidor. Tente novamente.');
    }
  });
})();
