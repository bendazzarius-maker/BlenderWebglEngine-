// Minimal audio fallback using HTMLAudioElement. Replace with Howler later if needed.

const sounds = new Map();

export function initAudio() {
  console.log("Audio system initialized (HTMLAudioElement fallback)");
}

export function registerAudioBuffer(url, name = 'sound') {
  const audio = new Audio(url);
  audio.preload = 'auto';
  sounds.set(name, audio);
  console.log('Audio loaded:', name);
}

// Optional helpers
export function play(name) {
  const a = sounds.get(name);
  if (a) a.play();
}
export function stop(name) {
  const a = sounds.get(name);
  if (a) { a.pause(); a.currentTime = 0; }
}
