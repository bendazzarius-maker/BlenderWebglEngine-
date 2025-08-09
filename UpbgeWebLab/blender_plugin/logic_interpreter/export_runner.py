"""Utilities to analyze objects and export graphs to JSON/JS."""

from __future__ import annotations

from datetime import datetime
from importlib import import_module
from typing import Dict, List

from .codegen_jsnode import generate_js_module
from .extract_upbge import build_graph_from_active_object, collect_game_properties
from .graph_model import Graph

PREFIX_MAP = {"sensor": "sens", "controller": "lg", "actuator": "act"}


def _import_brick_module(brick_type: str):
    category, name = brick_type.split(".")
    prefix = PREFIX_MAP[category]
    module_path = f"logic_brick_dictionary.{prefix}_{name}"
    return import_module(module_path)


def analyze_object_to_json_payload(obj) -> dict:
    """Return a JSON-serialisable payload for *obj*."""

    graph = build_graph_from_active_object(obj)
    nodes: List[dict] = []
    for node in graph.nodes.values():
        module = _import_brick_module(node.brick_type)
        nodes.append(module.serialize_instance(node.values))
    links = [
        {
            "src": {"node": l.src.node, "socket": l.src.socket},
            "dst": {"node": l.dst.node, "socket": l.dst.socket},
        }
        for l in graph.links
    ]
    payload = {
        "version": "1.0",
        "object": getattr(obj, "name", "Object"),
        "timestamp": datetime.utcnow().isoformat(),
        "nodes": nodes,
        "links": links,
        "game_properties": collect_game_properties(obj),
    }
    return payload


def get_js_module_for_object(obj) -> str:
    """Generate JS module string for *obj*."""

    graph = build_graph_from_active_object(obj)
    return generate_js_module(graph)


def register() -> None:
    """Placeholder register to follow block order."""


def unregister() -> None:
    """Placeholder unregister to follow block order."""
