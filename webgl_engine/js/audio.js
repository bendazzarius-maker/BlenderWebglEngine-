import { Howl } from '../libs/howler.core.js';

const sounds = new Map();

export function initAudio() {
  console.log("Audio system initialized");
}

export function registerAudioBuffer(url, name = 'sound') {
  const snd = new Howl({ src: [url], volume: 0.7 });
  sounds.set(name, snd);
  console.log('Audio loaded:', name);
}
