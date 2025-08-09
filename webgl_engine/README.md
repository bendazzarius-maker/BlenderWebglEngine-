# WebGL Engine Skeleton

This folder contains a minimal HTML5/JS/CSS scaffold for a WebGL game engine.
No binary dependencies are included. Place required libraries under `libs/`.

## TODO: Fetch Dependencies
- **three.module.js** — core 3D engine
- **OrbitControls.js** — Blender-like viewport navigation
- **GLTFLoader.js** — load glTF/GLB assets
- **stats.module.js** — FPS and performance monitor
- **howler.core.js** — audio playback
- *(optional)* `TransformControls.js` — gizmos for move/rotate/scale
- *(optional)* physics (cannon-es / ammo.js)
- *(optional)* particles (Three.js points or external lib)
- *(optional)* Monaco Editor + node graph (e.g., LiteGraph.js) for in-page IDE/JSNode

Copy the `.js` files into `webgl_engine/libs/` and keep imports in code pointing to `./libs/...`.

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
  libs/           # third-party libs (three, loaders, howler, stats)
  assets/
    models/
    textures/
    sounds/
```
