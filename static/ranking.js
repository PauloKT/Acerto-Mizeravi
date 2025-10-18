(function(){
  const tbody = document.querySelector('#rankingTable tbody');
  if(!tbody) return;
  
  const key = 'tabareli_ranking';
  
  function load(){ 
    const raw = localStorage.getItem(key); 
    return raw ? JSON.parse(raw) : []; 
  }
  
  function render(){
    const list = load();
    tbody.innerHTML = '';
    
    if(list.length === 0){ 
      tbody.innerHTML = '<tr><td colspan="3" style="text-align: center; padding: 20px;">Nenhum registro encontrado</td></tr>'; 
      return; 
    }
    
    // Ordenar por pontuação (maior primeiro)
    const sortedList = list.sort((a, b) => b.score - a.score);
    
    // Exibir top 100
    sortedList.slice(0, 100).forEach((record, index) => {
      const tr = document.createElement('tr');
      
      // Destacar o usuário atual se estiver logado
      const currentUser = localStorage.getItem('tabareli_current');
      const isCurrentUser = currentUser && record.name === currentUser;
      
      if (isCurrentUser) {
        tr.style.backgroundColor = 'rgba(255, 255, 0, 0.1)';
        tr.style.border = '1px solid #ffff00';
      }
      
      tr.innerHTML = `
        <td style="text-align: center; font-weight: bold;">${index + 1}</td>
        <td style="font-weight: ${isCurrentUser ? 'bold' : 'normal'}; color: ${isCurrentUser ? '#ffff00' : 'inherit'};">${record.name}</td>
        <td style="text-align: center; font-weight: bold;">${record.score.toLocaleString()}</td>
      `;
      
      tbody.appendChild(tr);
    });
  }
  
  // Verificar se há usuário logado
  const currentUser = localStorage.getItem('tabareli_current');
  if (!currentUser) {
    // Se não estiver logado, redirecionar para login
    window.location.href = 'login.html';
    return;
  }
  
  // Mostrar informações do usuário logado
  function showUserInfo() {
    const userDataRaw = localStorage.getItem('tabareli_user_data');
    const userData = userDataRaw ? JSON.parse(userDataRaw) : null;
    const welcomeUser = document.getElementById('welcomeUser');
    
    if (welcomeUser && userData) {
      welcomeUser.textContent = `Olá, ${userData.nome}! Veja sua posição no ranking:`;
    }
  }
  
  showUserInfo();
  render();
})();
