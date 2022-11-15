from __future__ import annotations
from visualizer import *


class BellmanFord:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph, start_node: int) -> None:
        self.graph = graph
        self.start_node = start_node

    def run(self) -> dict[int, int]:
        distances = {v: float('inf') for v in self.graph.nodes.keys()}
        distances[self.start_node] = 0

        for _ in range(len(self.graph.nodes) - 1):
            for edge in self.graph.edges:
                weight = self.graph[edge[0]][edge[1]]["weight"]
                if distances[edge[0]] != float("Inf") and distances[edge[0]] + weight < distances[edge[1]]:
                    distances[edge[1]] = distances[edge[0]] + weight

        return distances

    def draw(self, distances: dict) -> None:
        node_labels = {node: str(node) + " (" + str(distances[node]) + ")" for node in distances}

        GraphVisualizer(self.graph).\
            withNodeColor(self.start_node, 'red').\
            withNodeLabels(node_labels).\
            draw().\
            withWeight().\
            show()
