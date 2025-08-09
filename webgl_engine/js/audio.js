// Audio system that prefers Howler.js when available and falls back to
// HTMLAudioElement when Howler cannot be loaded.

let HowlLib = null;
const sounds = new Map();

export async function initAudio() {
  try {
    ({ Howl: HowlLib } = await import('howler'));
    console.log('Audio system initialized (Howler)');
  } catch {
    console.log('Audio system initialized (HTMLAudioElement fallback)');
  }
}

export function registerAudioBuffer(url, name = 'sound') {
  if (HowlLib) {
    const snd = new HowlLib({ src: [url], volume: 0.7 });
    sounds.set(name, snd);
  } else {
    const audio = new Audio(url);
    audio.preload = 'auto';
    sounds.set(name, audio);
  }
  console.log('Audio loaded:', name);
}

export function play(name) {
  const a = sounds.get(name);
  if (a?.play) a.play();
}

export function stop(name) {
  const a = sounds.get(name);
  if (!a) return;
  if (a.stop) {
    a.stop();
  } else {
    a.pause();
    a.currentTime = 0;
  }
}

