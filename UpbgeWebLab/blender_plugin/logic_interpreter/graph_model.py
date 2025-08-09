"""Graph model for logic brick export."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional


@dataclass
class SocketRef:
    node: str
    socket: str


@dataclass
class Node:
    node_id: str
    brick_type: str
    values: Dict[str, object]


@dataclass
class Link:
    src: SocketRef
    dst: SocketRef


@dataclass
class Graph:
    nodes: Dict[str, Node] = field(default_factory=dict)
    links: List[Link] = field(default_factory=list)

    def topo_order(self) -> List[Node]:
        """Return nodes in a basic topological order."""

        indegree = {nid: 0 for nid in self.nodes}
        adj: Dict[str, List[str]] = {nid: [] for nid in self.nodes}
        for link in self.links:
            adj[link.src.node].append(link.dst.node)
            indegree[link.dst.node] += 1

        queue = [nid for nid, deg in indegree.items() if deg == 0]
        ordered: List[Node] = []
        while queue:
            nid = queue.pop(0)
            ordered.append(self.nodes[nid])
            for m in adj[nid]:
                indegree[m] -= 1
                if indegree[m] == 0:
                    queue.append(m)
        return ordered


def register() -> None:
    """Placeholder register to follow block order."""


def unregister() -> None:
    """Placeholder unregister to follow block order."""
