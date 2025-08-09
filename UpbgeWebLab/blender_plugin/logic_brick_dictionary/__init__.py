# -*- coding: utf-8 -*-
"""Canonical access to logic brick dictionary modules."""

import os
import pkgutil
from pathlib import Path

# Include legacy dictionary folder with spaces
_legacy_dir = Path(__file__).resolve().parent.parent / 'LogicBrick Dictionnary '
if _legacy_dir.exists():
    __path__.append(str(_legacy_dir))

__all__ = [name for _, name, _ in pkgutil.iter_modules(__path__)]
