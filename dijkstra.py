from __future__ import annotations
from fibonacci import *
from visualizer import *


class Dijkstra:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph, start_node: int) -> None:
        self.graph = graph
        self.start_node = start_node

    def run(self) -> dict[int, int]:
        distances = {v: float('inf') for v in self.graph.nodes.keys()}
        distances[self.start_node] = 0

        visited = {}

        queue = FibonacciHeap()
        queue.insert(0, self.start_node)

        while not queue.is_empty():
            node = queue.extract_min()
            visited[node.value] = 0

            for neighbor in self.graph.neighbors(node.value):
                weight = self.graph[node.value][neighbor]["weight"]

                if neighbor not in visited:
                    cost = distances[node.value] + weight
                    if cost < distances[neighbor]:
                        queue.insert(cost, neighbor)
                        distances[neighbor] = cost

        return distances

    def draw(self, distances: dict) -> None:
        node_labels = {node: str(node) + " (" + str(distances[node]) + ")" for node in distances}

        GraphVisualizer(self.graph).\
            withNodeColor(self.start_node, 'red').\
            withNodeLabels(node_labels).\
            draw().\
            withWeight().\
            show()
