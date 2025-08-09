"""UPBGE Logic → JSNode Exporter add-on."""

from __future__ import annotations

bl_info = {
    "name": "UPBGE Logic → JSNode Exporter",
    "version": (0, 1, 0),
    "blender": (4, 3, 0),
    "category": "Game Engine",
}

from .logic_interpreter import ui_panel

_modules = [ui_panel]


def register() -> None:
    for mod in _modules:
        mod.register()


def unregister() -> None:
    for mod in reversed(_modules):
        mod.unregister()
