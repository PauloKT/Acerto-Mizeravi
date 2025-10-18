(function(){
  const tbody = document.querySelector('#rankingTable tbody');
  if(!tbody) return;
  const key = 'tabareli_ranking';
  function load(){ const raw = localStorage.getItem(key); return raw?JSON.parse(raw):[]; }
  function render(){
    const list = load();
    tbody.innerHTML = '';
    if(list.length===0){ tbody.innerHTML = '<tr><td colspan="3">Sem registros</td></tr>'; return; }
    list.slice(0,100).forEach((r,i)=>{
      const tr = document.createElement('tr');
      tr.innerHTML = `<td>${i+1}</td><td>${r.name}</td><td>${r.score}</td>`;
      tbody.appendChild(tr);
    });
  }
  render();
})();
