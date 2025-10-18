// login.js
(function(){
  const btn = document.getElementById('btnLogin');
  if(!btn) return;

  if(window.createShootingStars) window.createShootingStars();

  btn.addEventListener('click', async (e)=>{
    e.preventDefault();
    const emailOrLogin = document.getElementById('email').value.trim();
    const pwd = document.getElementById('pwd').value.trim();
    
    if(!emailOrLogin || !pwd){ 
      alert('Preencha todos os campos'); 
      return; 
    }

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          nome: emailOrLogin
        })
      });

      const data = await response.json();

      if (data.sucesso) {
        // Salvar dados do usuário no localStorage
        localStorage.setItem('tabareli_current', data.usuario.nome);
        localStorage.setItem('tabareli_user_data', JSON.stringify(data.usuario));
        
        try{ 
          new Audio('sound/click.mp3').play().catch(()=>{}); 
        }catch(e){}
        
        window.location.href = 'menu.html';
      } else {
        alert('Usuário não encontrado.');
      }
    } catch (error) {
      console.error('Erro ao fazer login:', error);
      alert('Erro ao conectar com o servidor. Tente novamente.');
    }
  });
})();
