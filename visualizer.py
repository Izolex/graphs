from __future__ import annotations
import matplotlib.pyplot as plt
from algorithm import *


class Visualizer:
    pos: dict
    context: AlgoContext
    result: AlgoResult

    colors: list[str] = ['coral', 'violet', 'dodgerblue', 'hotpink']

    def __init__(self, context: AlgoContext, result: AlgoResult):
        self.context = context
        self.result = result
        self.pos = networkx.spring_layout(self.context.graph)

    def __getEdgeColors(self):
        edge_color_list = []

        for edge in self.context.graph.edges():
            if edge in self.result.edge_colors:
                edge_color_list.append('red')
            else:
                edge_color_list.append('black')

        return edge_color_list

    def __getNodeLabels(self):
        labels = {}
        for node in self.context.graph.nodes:
            cols = []
            for i in range(0, len(self.result.node_labels)):
                cols.append(str(self.result.node_labels[i][node]))

            labels[node] = (' / '.join(cols) + ' - ' if len(cols) else '') + str(node)

        return labels

    def __getEdgeLabels(self):
        labels = {}
        for edge in self.context.graph.edges:
            cols = []
            for i in range(0, len(self.result.edge_labels)):
                cols.append(str(self.result.edge_labels[i][edge]))

            labels[edge] = ' / '.join(cols)

        return labels

    def __getNodeColors(self):
        if self.result.node_colors:
            colors = [self.colors[c] for c in self.result.node_colors]
        else:
            colors = ["lightblue"] * len(self.context.graph.nodes)

        if self.result.start_color:
            colors[self.context.start_node] = 'red'
        if self.result.end_color:
            colors[self.context.end_node] = 'blue'

        return colors

    def draw(self):
        node_labels = self.__getNodeLabels()
        networkx.draw_networkx_labels(self.context.graph, self.pos, node_labels)

        networkx.draw(
            self.context.graph,
            self.pos,
            with_labels=False,
            node_color=self.__getNodeColors(),
            edge_color=self.__getEdgeColors()
        )

        edge_labels = self.__getEdgeLabels()
        if len(edge_labels):
            networkx.draw_networkx_edge_labels(self.context.graph, self.pos, edge_labels)

        return self

    def show(self) -> None:
        plt.axis('off')
        plt.show()
