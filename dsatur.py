from __future__ import annotations
from visualizer import *


class DSatur:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def run(self) -> list[int]:
        nodes = []
        for idx, node in enumerate(self.graph.nodes):
            neighbors = len(list(self.graph.neighbors(node)))
            nodes.append((node, neighbors, idx))

        nodes.sort(reverse=True, key=lambda x: x[1])

        result = {nodes[0][0]: 0}
        nodes.pop(0)

        while len(result.items()) < len(self.graph.nodes):
            candidates = []

            for node in self.graph.nodes:
                if node in result:
                    continue

                coloring = {}
                neighbours = self.graph.neighbors(node)

                for neighbor in neighbours:
                    if neighbor in result:
                        if result[neighbor] in coloring:
                            coloring[result[neighbor]] += 1
                        else:
                            coloring[result[neighbor]] = 1

                candidates.append((node, len(coloring.items()), len(list(neighbours))))

            candidates.sort(reverse=True, key=lambda x: (x[1], x[2]))

            node = candidates.pop(0)

            color = -1
            while True:
                color += 1

                has_neighbour = False
                for neighbor in self.graph.neighbors(node[0]):
                    if neighbor in result and result[neighbor] == color:
                        has_neighbour = True
                        break

                if not has_neighbour:
                    result[node[0]] = color
                    break

        return [n[1] for n in sorted(result.items())]

    def draw(self, colors: list[int]) -> None:
        GraphVisualizer(self.graph).\
            withColoring(colors).\
            draw().\
            withWeight().\
            show()
