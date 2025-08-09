export function initOutliner(scene) {
    const list = document.getElementById('outliner-list');
    list.innerHTML = '';
    scene.traverse(obj => {
        if (obj.isMesh) {
            const li = document.createElement('li');
            li.textContent = obj.name || obj.type;
            list.appendChild(li);
        }
    });
}
