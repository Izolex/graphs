from __future__ import annotations

import matplotlib.pyplot as plt
import networkx
from networkx import Graph


class GraphVisualizer:
    g: Graph
    pos: dict
    edge_labels: bool = False
    with_labels: bool = True
    colors: list = []

    def __init__(self, g: Graph):
        self.g = g
        self.pos = networkx.spring_layout(g)

    def withNodeLabels(self, labels: dict) -> GraphVisualizer:
        networkx.draw_networkx_labels(self.g, self.pos, labels)
        self.with_labels = False

        return self

    def withColors(self, colors: list) -> GraphVisualizer:
        self.colors = colors

        return self

    def draw(self) -> GraphVisualizer:
        networkx.draw(
            self.g,
            self.pos,
            with_labels=self.with_labels,
            font_weight='bold',
            node_color=self.colors
        )

        return self

    def withEdgeLabels(self, labels: dict) -> GraphVisualizer:
        networkx.draw_networkx_edge_labels(self.g, self.pos, edge_labels=labels)

        return self

    def show(self) -> None:
        plt.axis('off')
        plt.show()
