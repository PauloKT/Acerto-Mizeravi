// Sistema de gerenciamento de áudio global
(function() {
  'use strict';
  
  // Variável global para o áudio
  let globalAudio = null;
  let isAudioInitialized = false;
  
  // Função para inicializar o áudio
  function initGlobalAudio() {
    if (isAudioInitialized) return;
    
    try {
      globalAudio = new Audio('sound/intro.mp3');
      globalAudio.volume = 0.2;
      globalAudio.loop = true;
      globalAudio.preload = 'auto';
      
      // Configurar eventos de áudio
      globalAudio.addEventListener('canplaythrough', function() {
        console.log('Áudio carregado e pronto para reprodução');
      });
      
      globalAudio.addEventListener('error', function(e) {
        console.error('Erro ao carregar áudio:', e);
      });
      
      isAudioInitialized = true;
      console.log('Sistema de áudio global inicializado');
    } catch (error) {
      console.error('Erro ao inicializar áudio:', error);
    }
  }
  
  // Função para tocar o áudio
  function playGlobalAudio() {
    if (!globalAudio || !isAudioInitialized) {
      initGlobalAudio();
    }
    
    if (globalAudio) {
      try {
        // Verificar se já está tocando
        if (!globalAudio.paused && globalAudio.currentTime > 0) {
          return;
        }
        
        globalAudio.currentTime = 0;
        const playPromise = globalAudio.play();
        
        if (playPromise !== undefined) {
          playPromise.then(() => {
            console.log('Áudio iniciado com sucesso');
          }).catch(error => {
            console.log('Erro ao reproduzir áudio (pode ser política do navegador):', error);
            // Não tentar novamente automaticamente, deixar para a interação do usuário
          });
        }
      } catch (error) {
        console.error('Erro ao tocar áudio:', error);
      }
    }
  }
  
  // Função para pausar o áudio
  function pauseGlobalAudio() {
    if (globalAudio) {
      try {
        globalAudio.pause();
        globalAudio.currentTime = 0;
        console.log('Áudio pausado');
      } catch (error) {
        console.error('Erro ao pausar áudio:', error);
      }
    }
  }
  
  // Função para parar o áudio
  function stopGlobalAudio() {
    if (globalAudio) {
      try {
        globalAudio.pause();
        globalAudio.currentTime = 0;
        console.log('Áudio parado');
      } catch (error) {
        console.error('Erro ao parar áudio:', error);
      }
    }
  }
  
  // Função para verificar se o áudio está tocando
  function isAudioPlaying() {
    return globalAudio && !globalAudio.paused && globalAudio.currentTime > 0;
  }
  
  // Inicializar quando a página carregar
  document.addEventListener('DOMContentLoaded', function() {
    initGlobalAudio();
    
    // Tentar tocar imediatamente
    setTimeout(() => {
      playGlobalAudio();
    }, 100);
    
    // Tentar novamente após um tempo maior
    setTimeout(() => {
      if (!isAudioPlaying()) {
        playGlobalAudio();
      }
    }, 1000);
  });
  
  // Tentar tocar após qualquer interação do usuário
  function tryPlayOnInteraction() {
    if (!isAudioPlaying()) {
      playGlobalAudio();
    }
  }
  
  document.addEventListener('click', tryPlayOnInteraction, { once: true });
  document.addEventListener('touchstart', tryPlayOnInteraction, { once: true });
  document.addEventListener('keydown', tryPlayOnInteraction, { once: true });
  document.addEventListener('mousemove', tryPlayOnInteraction, { once: true });
  
  // Parar áudio quando sair da página
  window.addEventListener('beforeunload', stopGlobalAudio);
  
  // Expor funções globalmente
  window.AudioManager = {
    play: playGlobalAudio,
    pause: pauseGlobalAudio,
    stop: stopGlobalAudio,
    isPlaying: isAudioPlaying,
    init: initGlobalAudio
  };
  
  console.log('AudioManager carregado');
})();
