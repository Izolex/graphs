from __future__ import annotations
from visualizer import *


class WelshPowell:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def run(self) -> list[int]:
        result = {}

        nodes = []
        for node in self.graph.nodes:
            neighbors = len(list(self.graph.neighbors(node)))
            nodes.append((neighbors, node))

        nodes.sort(reverse=True, key=lambda x: x[0])

        color = -1
        while len(result.items()) < len(self.graph.nodes):
            color += 1
            for node in nodes:
                has_neighbour = False
                for neighbor in self.graph.neighbors(node[1]):
                    if neighbor in result and result[neighbor] == color:
                        has_neighbour = True
                        break

                if node[1] not in result and not has_neighbour:
                    result[node[1]] = color

        return [n[1] for n in sorted(result.items())]

    def draw(self, colors: list[int]) -> None:
        GraphVisualizer(self.graph).\
            withColoring(colors).\
            draw().\
            withWeight().\
            show()
