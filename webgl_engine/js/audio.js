import { Howl } from '../libs/howler.core.js';

export function initAudio() {
    const sound = new Howl({
        src: ['assets/sounds/example.mp3'],
        volume: 0.5
    });
    console.log('Audio system initialized');
    return sound;
}
