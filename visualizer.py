from __future__ import annotations
import matplotlib.pyplot as plt
import networkx
from algorithm import *


class GraphVisualizer:
    g: Graph
    pos: dict
    edge_labels: bool = False
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

    def withNodeColors(self, colors: list[str]):
        self.node_colors = colors
        return self

    def withColoring(self, coloring: list[int]):
        self.node_colors = [self.colors[c] for c in coloring]
        return self

    def withEdgeColors(self) -> GraphVisualizer:
        self.with_edge_colors = True
        return self

    def drawNodeLabels(self, labels: dict) -> GraphVisualizer:
        networkx.draw_networkx_labels(self.graph, self.pos, labels)
        self.with_node_labels = False
        return self

    def drawGraph(self) -> GraphVisualizer:
        edge_color_list = []

        for edge in self.graph.edges():
            if 'color' in self.graph[edge[0]][edge[1]]:
                edge_color_list.append(self.graph[edge[0]][edge[1]]['color'])
            else:
                edge_color_list.append('black')

        networkx.draw(
            self.graph,
            self.pos,
            with_labels=self.with_node_labels,
            font_weight='bold',
            node_color=self.node_colors,
            edge_color=edge_color_list
        )

        return self

    def drawEdgeLabels(self, labels: dict) -> GraphVisualizer:
        networkx.draw_networkx_edge_labels(self.graph, self.pos, labels)
        return self

    def drawWeights(self) -> GraphVisualizer:
        labels = networkx.get_edge_attributes(self.graph, 'weight')
        return self.drawEdgeLabels(labels)

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
            drawGraph().\
            drawWeights().\
            show()

    def shortestPath(self, distances: dict[Graph.nodes, float]):
        node_labels = {node: str(node) + " (" + str(int(distances[node])) + ")" for node in distances}

        GraphVisualizer(self.context.graph).\
            withNodeColor(self.context.start_node, 'red').\
            drawNodeLabels(node_labels).\
            drawGraph().\
            drawWeights().\
            show()

    def coloring(self, colors: list[int]):
        GraphVisualizer(self.context.graph).\
            withColoring(colors).\
            drawGraph().\
            drawWeights().\
            show()

    def networkFlow(self, flow: dict[Graph.edges, int]):
        edge_labels = {e: str(int(flow[e])) + " / " + str(self.context.graph[e[0]][e[1]]['weight']) for e in flow}

        GraphVisualizer(self.context.graph).\
            withNodeColor(self.context.start_node, 'red').\
            withNodeColor(self.context.end_node, 'blue').\
            drawGraph().\
            drawEdgeLabels(edge_labels).\
            show()

