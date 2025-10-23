// login.js - Sistema de login usando endpoints da API
(function(){
  const btn = document.getElementById('btnLogin');
  if(!btn) return;

  if(window.createShootingStars) window.createShootingStars();

  btn.addEventListener('click', async (e)=>{
    e.preventDefault();
    const login = document.getElementById('email').value.trim();
    const senha = document.getElementById('pwd').value.trim();
    
    if(!login || !senha){ 
      alert('Preencha todos os campos'); 
      return; 
    }

    try {
      // Tentar fazer login via API
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          login: login,
          senha: senha
        })
      });

      const data = await response.json();

      if(data.sucesso) {
        // Salvar dados do usuário no sessionStorage
        sessionStorage.setItem('usuario_atual', JSON.stringify(data.usuario));
        try{ 
          new Audio('sound/click.mp3').play().catch(()=>{}); 
        }catch(e){}
        window.location.href = 'menu.html';
      } else {
        alert(data.erro || 'Erro no login');
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
      alert('Erro de conexão. Tente novamente.');
    }
  });
})();
