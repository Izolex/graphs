from __future__ import annotations
from visualizer import *

class RLF:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def run(self) -> list[int]:
        result = {}

        color = -1
        while len(result.items()) < len(self.graph.nodes):
            color += 1

            while True:
                candidates = []

                for node in self.graph.nodes:
                    if node in result:
                        continue

                    coloring = {}

                    has_neighbour = False
                    for neighbor in self.graph.neighbors(node):
                        if neighbor in result and result[neighbor] == color:
                            has_neighbour = True
                            break

                        for sub_neighbor in self.graph.neighbors(neighbor):
                            if sub_neighbor in coloring and sub_neighbor in result and result[sub_neighbor] == color:
                                coloring[sub_neighbor] += 1
                            else:
                                coloring[sub_neighbor] = 1

                    if has_neighbour:
                        continue

                    candidates.append((node, len(coloring.items())))

                if 0 == len(candidates):
                    break

                candidates.sort(reverse=True, key=lambda x: x[1])

                node = candidates.pop(0)
                result[node[0]] = color


        return [n[1] for n in sorted(result.items())]

    def draw(self, colors: list[int]) -> None:
        GraphVisualizer(self.graph).\
            withColoring(colors).\
            draw().\
            withWeight().\
            show()