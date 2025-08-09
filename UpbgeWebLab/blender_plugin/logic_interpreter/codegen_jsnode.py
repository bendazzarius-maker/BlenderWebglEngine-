"""Generate JavaScript code from logic brick graphs."""

from __future__ import annotations

from typing import Dict, List

from .graph_model import Graph, Node


def gen_node_js(node_type: str, values: dict, input_exprs: Dict[str, object]):
    """Return JS expressions and code lines for a node."""

    outputs: Dict[str, str] = {}
    code: List[str] = []
    category, name = node_type.split(".")

    if category == "sensor" and name == "keyboard":
        key = values.get("key", "")
        outputs["out_pressed"] = f"input.isKeyDown('{key}')"
    elif category == "controller" and name == "and":
        exprs = input_exprs.get("in_inputs", [])
        if isinstance(exprs, str):
            exprs = [exprs]
        expr = " && ".join(exprs) if exprs else "false"
        outputs["out_result"] = f"({expr})"
    elif category == "actuator" and name == "motion":
        trigger = input_exprs.get("in_trigger", "false")
        lin = values.get("lin_velocity", [0.0, 0.0, 0.0])
        ang = values.get("ang_velocity", [0.0, 0.0, 0.0])
        local = str(values.get("use_local", False)).lower()
        code.append(
            f"if ({trigger}) applyMotion({lin}, {ang}, {local});"
        )
    return {"outputs": outputs, "code": code}


def generate_js_module(graph: Graph) -> str:
    """Generate a small JavaScript module for *graph*."""

    lines: List[str] = ["export function run(input) {"]
    expr_map: Dict[tuple, str] = {}

    for node in graph.topo_order():
        input_exprs: Dict[str, List[str]] = {}
        for link in graph.links:
            if link.dst.node == node.node_id:
                src_expr = expr_map[(link.src.node, link.src.socket)]
                input_exprs.setdefault(link.dst.socket, []).append(src_expr)
        normalized: Dict[str, object] = {
            key: vals[0] if len(vals) == 1 else vals for key, vals in input_exprs.items()
        }
        generated = gen_node_js(node.brick_type, node.values, normalized)
        for out_id, expr in generated["outputs"].items():
            var = f"{node.node_id}_{out_id}"
            lines.append(f"  const {var} = {expr};")
            expr_map[(node.node_id, out_id)] = var
        for line in generated["code"]:
            lines.append(f"  {line}")
    lines.append("}")
    return "\n".join(lines)


def register() -> None:
    """Placeholder register to follow block order."""


def unregister() -> None:
    """Placeholder unregister to follow block order."""
