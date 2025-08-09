"""Extract logic bricks from the active object (stub implementation)."""

from __future__ import annotations

from datetime import datetime
from typing import List

from .graph_model import Graph, Link, Node, SocketRef


def build_graph_from_active_object(obj) -> Graph:
    """Build a graph from *obj*'s logic bricks.

    This environment lacks the UPBGE API, therefore a small example graph is
    returned so the export path can be exercised end-to-end.
    """

    # TODO: Replace stub with real extraction using bpy/UPBGE APIs.
    graph = Graph()
    graph.nodes["Keyboard"] = Node("Keyboard", "sensor.keyboard", {"key": "SPACE"})
    graph.nodes["And"] = Node("And", "controller.and", {})
    graph.nodes["Motion"] = Node(
        "Motion",
        "actuator.motion",
        {"lin_velocity": [1.0, 0.0, 0.0], "ang_velocity": [0.0, 0.0, 0.0], "use_local": True},
    )
    graph.links = [
        Link(SocketRef("Keyboard", "out_pressed"), SocketRef("And", "in_inputs")),
        Link(SocketRef("And", "out_result"), SocketRef("Motion", "in_trigger")),
    ]
    return graph


def collect_game_properties(obj) -> List[dict]:
    """Return game properties for *obj* applying the special ``texte`` rule."""

    # TODO: Fetch real game properties from *obj* when running inside UPBGE.
    example = [
        {"name": "score", "type": "Int", "value": 0, "mutable": True},
        {
            "name": "texte",
            "owner": getattr(obj, "name", "Object"),
            "type": "String",
            "value": "example",
            "mutable": False,
            "is_text_property": True,
        },
    ]
    return example


def register() -> None:
    """Placeholder register to follow block order."""


def unregister() -> None:
    """Placeholder unregister to follow block order."""
