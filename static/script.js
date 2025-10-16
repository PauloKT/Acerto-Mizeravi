// Registro
document.getElementById('registroForm').onsubmit = function(e) {
  e.preventDefault();
  const email = document.getElementById('email').value.trim();
  const nome = document.getElementById('nome').value.trim();
  if (!email || !nome) {
    document.getElementById('registroMsg').innerHTML = '<span class="erro">Preencha todos os campos.</span>';
    return;
  }
  localStorage.setItem('usuario', JSON.stringify({ email, nome }));
  document.getElementById('registroMsg').innerHTML = '<span class="msg">Registrado com sucesso!</span>';
  document.getElementById('registroForm').reset();
};

// Login
document.getElementById('loginForm').onsubmit = function(e) {
  e.preventDefault();
  const loginNome = document.getElementById('loginNome').value.trim();
  const usuario = JSON.parse(localStorage.getItem('usuario') || '{}');
  if (usuario.nome && usuario.nome === loginNome) {
    document.getElementById('loginMsg').innerHTML = '<span class="msg">Login realizado!</span>';
  } else {
    document.getElementById('loginMsg').innerHTML = '<span class="erro">Nome não encontrado.</span>';
  }
  document.getElementById('loginForm').reset();
};