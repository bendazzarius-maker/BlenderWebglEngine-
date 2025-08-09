// Simple tree with top-level containers
const CATS = ['Assets', 'Scripts', 'Runtime'];

export function initOutliner(scene) {
  const list = document.getElementById('outliner-list');
  list.innerHTML = '';
  for (const c of CATS) {
    const li = document.createElement('li');
    li.className = 'cat';
    li.textContent = c;
    const ul = document.createElement('ul');
    ul.dataset.cat = c;
    li.appendChild(ul);
    list.appendChild(li);
  }
  refreshOutliner(scene);
}

export function refreshOutliner(scene) {
  const assetsUL = document.querySelector('ul[data-cat="Assets"]');
  assetsUL.innerHTML = '';
  scene.traverse(obj => {
    if (obj.isMesh) {
      const li = document.createElement('li');
      li.textContent = obj.name || obj.type;
      assetsUL.appendChild(li);
    }
  });
}
