export function initUI(onPlay, onStop) {
    const playBtn = document.getElementById('playBtn');
    const stopBtn = document.getElementById('stopBtn');

    playBtn.addEventListener('click', () => {
        if (onPlay) onPlay();
    });

    stopBtn.addEventListener('click', () => {
        if (onStop) onStop();
    });
}
