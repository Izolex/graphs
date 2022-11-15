from __future__ import annotations
import matplotlib.pyplot as plt
import networkx
from networkx import Graph


class GraphVisualizer:
    g: Graph
    pos: dict
    edge_labels: bool = False
    with_labels: bool = True
    with_edge_colors: bool = False

    colors: list[str] = ['coral', 'violet', 'dodgerblue', 'hotpink']

    def __init__(self, g: Graph):
        self.graph = g
        self.pos = networkx.spring_layout(g)
        self.node_colors = ["lightblue"] * len(self.graph.nodes)

    def withNodeColor(self, node: int, color: str) -> GraphVisualizer:
        self.node_colors[node] = color
        return self

    def withNodeColors(self, colors: list[str]):
        self.node_colors = colors
        return self

    def withColoring(self, coloring: list[int]):
        self.node_colors = [self.colors[c] for c in coloring]
        return self

    def withNodeLabels(self, labels: dict) -> GraphVisualizer:
        networkx.draw_networkx_labels(self.graph, self.pos, labels)
        self.with_labels = False

        return self

    def withEdgeColors(self) -> GraphVisualizer:
        self.with_edge_colors = True

        return self

    def draw(self) -> GraphVisualizer:
        edge_color_list = []

        for edge in self.graph.edges():
            if 'color' in self.graph[edge[0]][edge[1]]:
                edge_color_list.append(self.graph[edge[0]][edge[1]]['color'])
            else:
                edge_color_list.append('black')

        networkx.draw(
            self.graph,
            self.pos,
            with_labels=self.with_labels,
            font_weight='bold',
            node_color=self.node_colors,
            edge_color=edge_color_list
        )

        return self

    def withWeight(self) -> GraphVisualizer:
        labels = networkx.get_edge_attributes(self.graph, 'weight')
        networkx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels)
        return self

    def withEdgeLabels(self, labels: dict) -> GraphVisualizer:
        networkx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels)

        return self

    def show(self) -> None:
        plt.axis('off')
        plt.show()
