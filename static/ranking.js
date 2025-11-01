// ranking.js - Sistema de ranking usando endpoints da API
(function(){
  const tbody = document.querySelector('#rankingTable tbody');
  if(!tbody) return;

  // Verificar se há usuário logado
  const usuarioAtual = sessionStorage.getItem('usuario_atual');
  if(!usuarioAtual){ 
    window.location.href = 'login.html'; 
    return; 
  }

  let rankingAtual = [];
  let categoriaSelecionada = 'geral';

  async function carregarRanking(categoria = 'geral'){
    try {
      tbody.innerHTML = '<tr><td colspan="3">Carregando ranking...</td></tr>';
      
      const url = categoria === 'geral' 
        ? '/api/ranking/geral' 
        : `/api/ranking/categoria/${categoria}`;
      
      const response = await fetch(url);
      const data = await response.json();
      
      if(data.sucesso) {
        rankingAtual = data.ranking;
        renderizarRanking(rankingAtual);
      } else {
        tbody.innerHTML = '<tr><td colspan="3">Erro ao carregar ranking</td></tr>';
      }
    } catch (error) {
      console.error('Erro ao carregar ranking:', error);
      tbody.innerHTML = '<tr><td colspan="3">Erro de conexão</td></tr>';
    }
  }

  function renderizarRanking(ranking){
    tbody.innerHTML = '';
    if(ranking.length === 0){ 
      tbody.innerHTML = '<tr><td colspan="3">Nenhum resultado encontrado</td></tr>'; 
      return; 
    }
    
    ranking.forEach((r, i) => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${i+1}</td>
        <td>${r.nome_usuario}</td>
        <td>${r.pontuacao_total} pts</td>
      `;
      tbody.appendChild(tr);
    });
  }

  // Carregar ranking inicial
  carregarRanking();

  // Adicionar filtros de categoria se existirem
  const categoriaSelect = document.getElementById('categoria-ranking');
  if(categoriaSelect) {
    categoriaSelect.addEventListener('change', (e) => {
      categoriaSelecionada = e.target.value;
      carregarRanking(categoriaSelecionada);
    });
  }

  // Expor função para recarregar ranking
  window.recarregarRanking = () => {
    carregarRanking(categoriaSelecionada);
  };
})();
