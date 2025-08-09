"""Aggregate logic brick dictionaries for the plugin.

This package exposes a ``logic_bricks`` dictionary containing all logic
brick definitions found in the submodules. Each submodule defines either
an ``actuator``, ``controller`` or ``sensor`` dictionary. They are
collected here for easy lookup by name.
"""

import importlib
import pkgutil
from typing import Dict, Any

logic_bricks: Dict[str, Dict[str, Any]] = {}

for module_info in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_info.name}")
    for key in ("actuator", "controller", "sensor"):
        if hasattr(module, key):
            brick = getattr(module, key)
            name = brick.get("name")
            if name:
                logic_bricks[name] = brick

__all__ = ["logic_bricks"]
