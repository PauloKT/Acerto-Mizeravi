(function(){
  if(!document.getElementById('questionText')) return;

  const click = new Audio('sound/click.mp3'); click.volume = 0.5; click.preload = 'auto';
 
  const correctS = new Audio('sound/corret.wav'); correctS.volume = 0.75; correctS.preload = 'auto';
  const wrongS = new Audio('sound/wrong.wav'); wrongS.volume = 0.75; wrongS.preload = 'auto';
  const bg = new Audio('sound/intro.mp3'); bg.loop=true; bg.volume=0.18; bg.preload = 'auto';

  function safePlay(a){
    try{
      a.currentTime = 0;
      const p = a.play();
      if(p && p.catch) p.catch(()=>{});
    }catch(e){}
  }

  // DOM refs
  const playerNameLabel = document.getElementById('playerNameLabel');
  const modeLabel = document.getElementById('modeLabel');
  const livesBadge = document.getElementById('livesBadge');
  const scoreBadge = document.getElementById('scoreBadge');
  const streakBadge = document.getElementById('streakBadge');
  const multBadge = document.getElementById('multBadge');
  const questionText = document.getElementById('questionText');
  const answersWrap = document.getElementById('answersWrap');
  const btnQuit = document.getElementById('btnQuit');

  // config
  const MODE = {
    facil:{label:'Fácil', lives:4, diff:'facil'},
    medio:{label:'Médio', lives:3, diff:'medio'},
    dificil:{label:'Difícil', lives:2, diff:'dificil'},
    mortesubita:{label:'Morte Súbita', lives:1, diff:'dificil'}
  };
  const POINTS = {facil:10, medio:25, dificil:50};
  const MULT = [{streak:30,m:10},{streak:20,m:4},{streak:10,m:2}];

  // QUESTIONS - expand as needed
  const QUESTIONS = [
    {q:'Qual é a capital do Brasil?', a:['São Paulo','Brasília','Rio de Janeiro','Belo Horizonte'], correct:1, diff:'facil'},
    {q:'Em HTML, qual tag cria um parágrafo?', a:['<p>','<para>','<paragraph>','<txt>'], correct:0, diff:'facil'},
    {q:'Quantos lados tem um hexágono?', a:['5','6','7','8'], correct:1, diff:'facil'},
    {q:'Quem pintou a Mona Lisa?', a:['Van Gogh','Picasso','Leonardo da Vinci','Rembrandt'], correct:2, diff:'medio'},
    {q:'Qual é a fórmula da água?', a:['H2O','CO2','O2','NaCl'], correct:0, diff:'facil'},
    {q:'Em que ano o homem pisou na Lua?', a:['1959','1969','1979','1989'], correct:1, diff:'medio'},
    {q:'Qual o maior planeta do Sistema Solar?', a:['Terra','Marte','Júpiter','Saturno'], correct:2, diff:'medio'},
    {q:'Quem escreveu "Dom Quixote"?', a:['Cervantes','Tolstói','Camões','Shakespeare'], correct:0, diff:'dificil'},
    {q:'Teorema de Pitágoras é?', a:['a^2 + b^2 = c^2','a+b=c','ab=c^2','a^2 - b^2 = c^2'], correct:0, diff:'dificil'},
    {q:'Em JS, qual palavra declara constante?', a:['var','let','const','static'], correct:2, diff:'medio'}
  ];

  // state
  let state = { user:null, mode:'facil', lives:0, score:0, streak:0, multiplier:1, currentQ:null, asked:[] };

  // helpers
  function getCurrent(){ return localStorage.getItem('tabareli_current'); }
  function getUser(login){ const raw=localStorage.getItem('tabareli_users'); if(!raw) return null; const arr=JSON.parse(raw); return arr.find(u=>u.login===login||u.email===login)||null; }
  function shuffle(arr){ const a=arr.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]] } return a; }

  function pickQuestion(pref){
    const pool = QUESTIONS.filter(q=>q.diff===pref);
    let q; let attempt=0;
    do{ q = pool[Math.floor(Math.random()*pool.length)] || QUESTIONS[Math.floor(Math.random()*QUESTIONS.length)]; attempt++; } while(state.asked.includes(q.q) && attempt<50);
    state.asked.push(q.q);
    if(state.asked.length>QUESTIONS.length) state.asked=[];
    return JSON.parse(JSON.stringify(q));
  }

  function calcMultiplier(streak){
    for(const m of MULT) if(streak>=m.streak) return m.m;
    return 1;
  }

  function updateUI(){
    if(playerNameLabel) playerNameLabel.textContent = state.user? state.user.name : 'Jogador';
    if(modeLabel) modeLabel.textContent = `Modo: ${MODE[state.mode].label}`;
    if(livesBadge) livesBadge.textContent = `Vidas: ${state.lives}`;
    if(scoreBadge) scoreBadge.textContent = `Pontos: ${state.score}`;
    if(streakBadge) streakBadge.textContent = `Seq: ${state.streak}`;
    if(multBadge) multBadge.textContent = `x${state.multiplier}`;
  }

  function renderQuestion(){
    if(!state.currentQ){ questionText.textContent = 'Aguardando...'; answersWrap.innerHTML=''; return; }
    questionText.textContent = state.currentQ.q;
    answersWrap.innerHTML = '';
    const order = shuffle([0,1,2,3]);
    order.forEach(i=>{
      const btn = document.createElement('button');
      btn.className = 'answer';
      btn.type = 'button';
      btn.innerHTML = `<strong>${String.fromCharCode(65+i)}</strong> ${state.currentQ.a[i]}`;
      btn.addEventListener('click', ()=> handleAnswer(i, btn));
      answersWrap.appendChild(btn);
    });
  }

  function handleAnswer(idx, btn){
    Array.from(answersWrap.children).forEach(b=>b.disabled=true);
    const correctIdx = state.currentQ.correct;
    if(idx === correctIdx){
      btn.classList.add('correct');
      safePlay(correctS);
      state.streak += 1;
      state.multiplier = calcMultiplier(state.streak);
      state.score += (POINTS[state.currentQ.diff] || 0) * state.multiplier;
    } else {
      btn.classList.add('wrong');
      safePlay(wrongS);
      state.streak = 0;
      state.multiplier = 1;
      state.lives -= 1;
    }
    updateUI();
    setTimeout(()=>{
      if(state.lives <= 0) endGame();
      else {
        state.currentQ = pickQuestion(MODE[state.mode].diff);
        renderQuestion();
      }
    },700);
  }

  function endGame(){
    localStorage.setItem('lastScore', state.score);
    const key='tabareli_ranking';
    const raw = localStorage.getItem(key); const arr = raw?JSON.parse(raw):[];
    arr.push({name: state.user? state.user.name : 'Anon', score: state.score, date: new Date().toISOString()});
    arr.sort((a,b)=>b.score - a.score);
    localStorage.setItem(key, JSON.stringify(arr.slice(0,200)));
    try{ new Audio('sound/gameover.mp3').play().catch(()=>{}); }catch(e){}
    setTimeout(()=> window.location.href='gameover.html', 700);
  }

  // init
  function init(){
    const current = getCurrent(); if(!current){ window.location.href='login.html'; return; }
    state.user = getUser(current);
    const chosen = localStorage.getItem('tabareli_chosen_mode') || 'facil';
    state.mode = chosen;
    state.lives = MODE[chosen].lives;
    state.score = 0; state.streak = 0; state.multiplier = 1; state.asked = [];
    state.currentQ = pickQuestion(MODE[chosen].diff);
    updateUI(); renderQuestion();

    function startBG(){ try{ bg.currentTime=0; bg.play().catch(()=>{}); }catch(e){}
      document.removeEventListener('click', startBG);
      document.removeEventListener('touchstart', startBG);
      document.removeEventListener('keydown', startBG);
    }
    document.addEventListener('click', startBG, { once:true });
    document.addEventListener('touchstart', startBG, { once:true });
    document.addEventListener('keydown', startBG, { once:true });
  }

  // quit button
  if(btnQuit) btnQuit.addEventListener('click', ()=>{ if(confirm('Deseja desistir e voltar ao menu?')){ try{ bg.pause(); }catch(e){} window.location.href='menu.html'; } });

  // keyboard A-D
  document.addEventListener('keydown', (e)=>{
    if(!state.currentQ) return;
    const k = e.key.toUpperCase();
    if(['A','B','C','D'].includes(k)){
      const idx = k.charCodeAt(0)-65;
      const btns = Array.from(answersWrap.children);
      const found = btns.find(b => b.textContent.trim().startsWith(String.fromCharCode(65+idx)));
      if(found && !found.disabled) found.click();
    }
  });

  init();
})();
