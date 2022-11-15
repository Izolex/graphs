from __future__ import annotations
from dataclasses import dataclass

import networkx
from networkx import Graph


@dataclass
class AlgoContext:
    graph: Graph
    start_node: int
    end_node: int


class AlgoResult:
    context: AlgoContext
    start_color: bool = False
    end_color: bool = False
    edge_labels: [dict[Graph.edges, str | int | float]] = []
    edge_colors: [list[Graph.edges]] = []
    node_labels: [dict[int, str | int | float]] = []
    node_colors: [list[int]] = []

    def __init__(self, context: AlgoContext):
        self.context = context

    def withStartColor(self) -> AlgoResult:
        self.start_color = True
        return self

    def withEndColor(self) -> AlgoResult:
        self.end_color = True
        return self

    def withEdgeLabels(self, labels: dict[Graph.edges, str | int | float]) -> AlgoResult:
        self.edge_labels.append(labels)
        return self

    def withNodeLabels(self, labels: dict[int, str | int | float]) -> AlgoResult:
        self.node_labels.append(labels)
        return self

    def withNodeColors(self, colors: list[int]) -> AlgoResult:
        self.node_colors = colors
        return self

    def withEdgeColors(self, colors: list[Graph.edges]) -> AlgoResult:
        self.edge_colors = colors
        return self

    def withWeights(self) -> AlgoResult:
        labels = networkx.get_edge_attributes(self.context.graph, 'weight')
        self.edge_labels.append(labels)
        return self
