from __future__ import annotations
import matplotlib.pyplot as plt
import networkx
from algorithm import *


class GraphVisualizer:
    g: Graph
    pos: dict
    edge_labels: dict[Graph.edges, str] = {}
    node_labels: dict[Graph.nodes, str] = {}
    with_node_labels: bool = True
    with_edge_colors: bool = False

    colors: list[str] = ['coral', 'violet', 'dodgerblue', 'hotpink']

    def __init__(self, g: Graph):
        self.graph = g
        self.pos = networkx.spring_layout(g)
        self.node_colors = ["lightblue"] * len(self.graph.nodes)

    def withNodeColor(self, node: int, color: str) -> GraphVisualizer:
        self.node_colors[node] = color
        return self

    def withNodeColors(self, colors: list[str]) -> GraphVisualizer:
        self.node_colors = colors
        return self

    def withColoring(self, coloring: list[int]) -> GraphVisualizer:
        self.node_colors = [self.colors[c] for c in coloring]
        return self

    def withEdgeColors(self) -> GraphVisualizer:
        self.with_edge_colors = True
        return self

    def withEdgeLabels(self, labels: dict[Graph.edges, str]) -> GraphVisualizer:
        self.edge_labels = labels
        return self

    def withWeights(self) -> GraphVisualizer:
        labels = networkx.get_edge_attributes(self.graph, 'weight')
        self.withEdgeLabels(labels)
        return self

    def withNodeLabels(self, labels: dict[Graph.nodes, str]) -> GraphVisualizer:
        self.node_labels = labels
        return self

    def draw(self) -> GraphVisualizer:
        edge_color_list = []

        for edge in self.graph.edges():
            if 'color' in self.graph[edge[0]][edge[1]]:
                edge_color_list.append(self.graph[edge[0]][edge[1]]['color'])
            else:
                edge_color_list.append('black')

        has_node_labels = bool(len(self.node_labels.items()))

        if has_node_labels:
            networkx.draw_networkx_labels(self.graph, self.pos, self.node_labels)

        networkx.draw(
            self.graph,
            self.pos,
            with_labels=not has_node_labels,
            font_weight='bold',
            node_color=self.node_colors,
            edge_color=edge_color_list
        )

        if len(self.edge_labels.items()):
            networkx.draw_networkx_edge_labels(self.graph, self.pos, self.edge_labels)

        return self

    def show(self) -> None:
        plt.axis('off')
        plt.show()


class GraphDrawer:
    context: AlgoContext

    def __init__(self, context: AlgoContext):
        self.context = context

    def minimalSpanningTree(self, edges: list[Graph.edges]):
        for edge in edges:
            self.context.graph[edge[0]][edge[1]]['color'] = 'red'

        GraphVisualizer(self.context.graph).\
            withEdgeColors().\
            withWeights().\
            draw().\
            show()

    def shortestPath(self, distances: dict[Graph.nodes, float]):
        node_labels = {node: str(node) + " (" + str(distances[node]) + ")" for node in distances}

        GraphVisualizer(self.context.graph).\
            withNodeColor(self.context.start_node, 'red').\
            withNodeLabels(node_labels).\
            withWeights().\
            draw().\
            show()

    def coloring(self, colors: list[int]):
        GraphVisualizer(self.context.graph).\
            withColoring(colors).\
            withWeights().\
            draw().\
            show()

    def networkFlow(self, flow: dict[Graph.edges, int]):
        labels = {}
        for e in self.context.graph.edges:
            labels[e] = str(int(flow[e])) + " / " + str(self.context.graph[e[0]][e[1]]['weight'])

        GraphVisualizer(self.context.graph).\
            withNodeColor(self.context.start_node, 'red').\
            withNodeColor(self.context.end_node, 'blue').\
            withEdgeLabels(labels).\
            draw().\
            show()
