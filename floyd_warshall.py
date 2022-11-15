from __future__ import annotations

from numpy import ndarray

from visualizer import *
import numpy


class FloydWarshall:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph, start_node: int) -> None:
        self.graph = graph
        self.start_node = start_node

    def run(self) -> ndarray[float]:
        edges_len = len(self.graph.edges)

        dist = numpy.full((edges_len, edges_len), float('inf'), float)

        for edge in self.graph.edges:
            dist[edge[0]][edge[1]] = self.graph[edge[0]][edge[1]]['weight']

        for node in self.graph.nodes:
            dist[node][node] = 0

        for k in range(edges_len):
            for i in range(edges_len):
                for j in range(edges_len):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = min(
                            dist[i][j],
                            dist[i][k] + dist[k][j]
                        )

        return dist

    def draw(self, dist: ndarray[float]) -> None:
        node_labels = {node: str(node) + " (" + str(int(dist[self.start_node][node])) + ")" for node in self.graph.nodes}

        GraphVisualizer(self.graph). \
            withNodeColor(self.start_node, 'red'). \
            withNodeLabels(node_labels). \
            draw(). \
            withWeight(). \
            show()
