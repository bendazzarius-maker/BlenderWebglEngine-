# WebGL Engine Skeleton

This folder contains a minimal HTML5/JS/CSS scaffold for a WebGL game engine.
No binary dependencies are committed. Dependencies are resolved via an import map
to `../node_builder/node_modules/`.

## TODO: Fetch Dependencies
- **three** — core 3D engine
- **OrbitControls** — Blender-like viewport navigation
- **GLTFLoader** — load glTF/GLB assets
- **stats.js** — FPS and performance monitor
- **howler** (optional) — audio playback
- *(optional)* `TransformControls.js` — gizmos for move/rotate/scale
- *(optional)* physics (cannon-es / ammo.js)
- *(optional)* particles (Three.js points or external lib)
- *(optional)* Monaco Editor + node graph (e.g., LiteGraph.js) for in-page IDE/JSNode

Dependencies should be installed under `../node_builder/node_modules/` and
referenced via the import map in `index.html`.

## Local Development

Serve the folder over **HTTP** so ES modules and APIs work correctly:

```bash
cd webgl_engine
python3 -m http.server 8080
# then open http://localhost:8080/
```

Alternatively, run:

- `webgl_engine/open_local.py` (opens index.html in your default browser), or
- any static server (e.g., `npx serve`).

## Structure

```
webgl_engine/
  index.html
  css/style.css
  js/
    main.js
    outliner.js
    audio.js
    gamepad.js
  assets/
    models/
    textures/
    sounds/
```
