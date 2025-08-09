# -*- coding: utf-8 -*-
"""Validate logic brick specifications."""

import importlib
import pkgutil
import sys
from pathlib import Path
from typing import List

if __package__ is None:
    # Ensure parent directory is on sys.path when executed as a script
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
PACKAGE = __package__ or "logic_brick_dictionary"

PREFIX_MAP = {
    "sensor": "sens",
    "controller": "lg",
    "actuator": "act",
}


def quick_spec_lookup(brick_type: str):
    """Return LOGIC_BRICK_SPEC for *brick_type* (e.g. ``sensor.keyboard``)."""
    category, name = brick_type.split(".")
    prefix = PREFIX_MAP.get(category)
    if not prefix:
        raise ValueError(f"Unknown category: {category}")
    module_name = f"{prefix}_{name}"
    module = importlib.import_module(f".{module_name}", PACKAGE)
    return getattr(module, "LOGIC_BRICK_SPEC", None)


def _validate_spec(mod_name: str, spec: dict, errors: List[str]):
    required_keys = {"id", "label", "category", "version", "sockets", "properties", "codegen"}
    missing = required_keys - spec.keys()
    if missing:
        errors.append(f"{mod_name}: missing keys {sorted(missing)}")
        return

    for direction in ("inputs", "outputs"):
        for sock in spec["sockets"].get(direction, []):
            for key in ("name", "id", "type", "default"):
                if key not in sock:
                    errors.append(f"{mod_name}: socket {sock.get('id', '?')} missing {key}")


if __name__ == "__main__":
    errors: List[str] = []
    pkg = importlib.import_module(PACKAGE)
    for _, mod_name, _ in pkgutil.iter_modules(pkg.__path__):
        if mod_name == "validate_logic_bricks":
            continue
        try:
            module = importlib.import_module(f"{PACKAGE}.{mod_name}")
        except Exception as exc:  # noqa: BLE001 - report any import failure
            errors.append(f"{mod_name}: import failed ({exc})")
            continue
        spec = getattr(module, "LOGIC_BRICK_SPEC", None)
        if spec is None:
            errors.append(f"{mod_name}: missing LOGIC_BRICK_SPEC")
            continue
        _validate_spec(mod_name, spec, errors)

    if errors:
        for err in errors:
            print(err)
        sys.exit(1)
    print("All logic brick specs validated successfully.")
    sys.exit(0)
