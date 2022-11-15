from __future__ import annotations
from dataclasses import dataclass
from networkx import Graph


@dataclass
class AlgoContext:
    graph: Graph
    start_node: int
