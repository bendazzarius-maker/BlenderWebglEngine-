export function initGamepad() {
    window.addEventListener('gamepadconnected', e => {
        console.log('Gamepad connected:', e.gamepad.id);
    });
    window.addEventListener('gamepaddisconnected', e => {
        console.log('Gamepad disconnected:', e.gamepad.id);
    });
}
