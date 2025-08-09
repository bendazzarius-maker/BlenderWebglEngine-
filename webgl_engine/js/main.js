// Block 1: imports
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import Stats from 'stats.js';
import { initOutliner, refreshOutliner } from './outliner.js';
import { initGamepad } from './gamepad.js';
import { initAudio, registerAudioBuffer } from './audio.js';

// Block 2: state
export const engine = {
  scene: null, camera: null, renderer: null, controls: null, stats: null,
  grid: null, axes: null, playing: false, clock: new THREE.Clock(), mixers: [],
  cube: null, particles: null
};

// Block 3+: init & runtime
init(); animate();

function init() {
  engine.scene = new THREE.Scene();
  engine.scene.background = new THREE.Color(0x222222);

  engine.camera = new THREE.PerspectiveCamera(60, 1, 0.1, 1000);
  engine.camera.position.set(4, 3, 6);

  engine.renderer = new THREE.WebGLRenderer({ antialias: true });
  const vp = document.getElementById('viewport');
  resize(); vp.appendChild(engine.renderer.domElement);
  window.addEventListener('resize', resize);

  engine.controls = new OrbitControls(engine.camera, engine.renderer.domElement);
  engine.controls.enableDamping = true;
  engine.controls.screenSpacePanning = true;

  engine.grid = new THREE.GridHelper(100, 100, 0x666666, 0x333333);
  engine.axes = new THREE.AxesHelper(1.5);
  engine.scene.add(engine.grid); engine.scene.add(engine.axes);

  engine.scene.add(new THREE.HemisphereLight(0xffffff, 0x444444, 1));
  const dir = new THREE.DirectionalLight(0xffffff, 0.8);
  dir.position.set(5, 10, 7.5); engine.scene.add(dir);

  // Example cube
  const geo = new THREE.BoxGeometry();
  const mat = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
  engine.cube = new THREE.Mesh(geo, mat);
  engine.scene.add(engine.cube);

  // Simple particle system
  const pGeo = new THREE.BufferGeometry();
  const count = 1000;
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < count * 3; i++) {
    positions[i] = (Math.random() - 0.5) * 10;
  }
  pGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  const pMat = new THREE.PointsMaterial({ color: 0xffffff, size: 0.05 });
  engine.particles = new THREE.Points(pGeo, pMat);
  engine.scene.add(engine.particles);

  engine.stats = new Stats(); document.body.appendChild(engine.stats.dom);

  initOutliner(engine.scene);
  initGamepad();
  initAudio();

  wireUI();
  enableDragDrop();
}

function resize() {
  const vp = document.getElementById('viewport');
  const w = vp.clientWidth || (window.innerWidth - 200);
  const h = vp.clientHeight || (window.innerHeight - 30);
  engine.camera.aspect = w / h; engine.camera.updateProjectionMatrix();
  engine.renderer.setSize(w, h);
}

function animate() {
  requestAnimationFrame(animate);
  if (engine.playing) {
    const dt = engine.clock.getDelta();
    for (const m of engine.mixers) m.update(dt);
    if (engine.cube) {
      engine.cube.rotation.x += 0.01;
      engine.cube.rotation.y += 0.01;
    }
  }
  engine.controls.update(); engine.stats.update();
  engine.renderer.render(engine.scene, engine.camera);
}

// === UI wiring ===
function wireUI() {
  const fileBtn = document.getElementById('fileBtn');
  const fileMenu = document.getElementById('fileMenu');
  fileBtn.onclick = () => fileMenu.classList.toggle('open');

  const editBtn = document.getElementById('editBtn');
  const editMenu = document.getElementById('editMenu');
  editBtn.onclick = () => editMenu.classList.toggle('open');

  const viewBtn = document.getElementById('viewBtn');
  const viewMenu = document.getElementById('viewMenu');
  viewBtn.onclick = () => viewMenu.classList.toggle('open');

  document.getElementById('toggleGrid').onclick = () => { engine.grid.visible = !engine.grid.visible; };
  document.getElementById('toggleAxes').onclick = () => { engine.axes.visible = !engine.axes.visible; };

  document.getElementById('playBtn').onclick = () => {
    engine.playing = true;
    document.getElementById('playBtn').disabled = true;
    document.getElementById('stopBtn').disabled = false;
  };
  document.getElementById('stopBtn').onclick = () => {
    engine.playing = false;
    document.getElementById('playBtn').disabled = false;
    document.getElementById('stopBtn').disabled = true;
  };

  document.getElementById('importModel').onclick = () => {
    document.getElementById('filePickerModel').click();
  };
  document.getElementById('filePickerModel').onchange = async e => {
    const file = e.target.files[0]; if (!file) return;
    await importModelFile(file);
  };

  document.getElementById('importAudio').onclick = () => {
    document.getElementById('filePickerAudio').click();
  };
  document.getElementById('filePickerAudio').onchange = async e => {
    const file = e.target.files[0]; if (!file) return;
    const url = URL.createObjectURL(file);
    registerAudioBuffer(url, file.name);
  };

  document.getElementById('openIDE').onclick = () => {
    alert('IDE/Node editor stub — TODO: integrate Monaco + node graph. Will emit JSNode.');
  };
  document.getElementById('renameItem').onclick = () => {
    alert('Rename stub — TODO: hook to current selection from Outliner.');
  };

  window.addEventListener('click', (ev) => {
    if (!ev.target.closest('.menu')) {
      for (const d of document.querySelectorAll('.dropdown')) d.classList.remove('open');
    }
  });
}

function enableDragDrop() {
  const vp = document.getElementById('viewport');
  vp.addEventListener('dragover', e => { e.preventDefault(); });
  vp.addEventListener('drop', async e => {
    e.preventDefault();
    const file = e.dataTransfer.files?.[0];
    if (file) await importModelFile(file);
  });
}

// === Loaders ===
async function importModelFile(file) {
  const url = URL.createObjectURL(file);
  const loader = new GLTFLoader();
  loader.load(url, gltf => {
    const root = gltf.scene || gltf.scenes[0];
    root.name = file.name.replace(/\.[^.]+$/, '');
    engine.scene.add(root);

    if (gltf.animations?.length) {
      const mixer = new THREE.AnimationMixer(root);
      engine.mixers.push(mixer);
      const action = mixer.clipAction(gltf.animations[0]);
      action.play();
    }

    refreshOutliner(engine.scene);
  }, undefined, err => {
    console.error('GLTF load error:', err);
  });
}
