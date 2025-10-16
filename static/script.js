
async function fazerRequisicao(url, dados) {
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dados)
    });
    return await response.json();
  } catch (error) {
    console.error('Erro na requisição:', error);
    return { sucesso: false, erro: 'Erro de conexão' };
  }
}


const registroForm = document.getElementById('registroForm');
if (registroForm) {
  registroForm.onsubmit = async function(e) {
    e.preventDefault();
    const email = document.getElementById('email').value.trim();
    const nome = document.getElementById('nome').value.trim();
    
    if (!email || !nome) {
      document.getElementById('registroMsg').innerHTML = '<span class="erro">Preencha todos os campos.</span>';
      return;
    }

    const resultado = await fazerRequisicao('/api/registrar', { email, nome });
    
    if (resultado.sucesso) {
      document.getElementById('registroMsg').innerHTML = '<span class="msg">Registrado com sucesso! Redirecionando...</span>';
      setTimeout(() => {
        window.location.href = '/';
      }, 2000);
    } else {
      const erro = resultado.erro || resultado.erros?.join(', ') || 'Erro no registro';
      document.getElementById('registroMsg').innerHTML = `<span class="erro">${erro}</span>`;
    }
  };
}


const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.onsubmit = async function(e) {
    e.preventDefault();
    const loginNome = document.getElementById('loginNome').value.trim();
    
    if (!loginNome) {
      document.getElementById('loginMsg').innerHTML = '<span class="erro">Nome é obrigatório.</span>';
      return;
    }

    const resultado = await fazerRequisicao('/api/login', { nome: loginNome });
    
    if (resultado.sucesso) {
      document.getElementById('loginMsg').innerHTML = '<span class="msg">Login realizado com sucesso!</span>';
      // Salvar dados do usuário no localStorage
      localStorage.setItem('usuario', JSON.stringify(resultado.usuario));
      // Redirecionar para uma página de dashboard ou área logada
      setTimeout(() => {
        alert('Login realizado! Bem-vindo, ' + resultado.usuario.nome);
      }, 1000);
    } else {
      const erro = resultado.erro || 'Erro no login';
      document.getElementById('loginMsg').innerHTML = `<span class="erro">${erro}</span>`;
    }
  };
}