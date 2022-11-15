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
    edge_labels: [] = []
    edge_colors: [] = []
    node_labels: [] = []
    node_colors: [] = []

    def __init__(self, context: AlgoContext):
        self.context = context

    def withStartColor(self):
        self.start_color = True
        return self

    def withEndColor(self):
        self.end_color = True
        return self

    def withEdgeLabels(self, labels: dict[Graph.edges, str | int | float]):
        self.edge_labels.append(labels)
        return self

    def withNodeLabels(self, labels: dict[int, str | int | float]):
        self.node_labels.append(labels)
        return self

    def withNodeColors(self, colors: list[int]):
        self.node_colors = colors
        return self

    def withEdgeColors(self, colors: list[Graph.edges]):
        self.edge_colors = colors
        return self

    def withWeights(self):
        labels = networkx.get_edge_attributes(self.context.graph, 'weight')
        self.edge_labels.append(labels)
        return self
