from __future__ import annotations
from fibonacci import *
from visualizer import *


class Prim:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph, start_node: int) -> None:
        self.graph = graph
        self.start_node = start_node

    def run(self) -> dict[int, int]:
        key = {v: float('inf') for v in self.graph.nodes.keys()}
        key[self.start_node] = 0

        mst = {v: -1 for v in self.graph.nodes.keys()}
        in_mst = {v: False for v in self.graph.nodes.keys()}

        queue = FibonacciHeap()
        queue.insert(0, self.start_node)
        key[self.start_node] = 0

        while not queue.is_empty():
            node = queue.extract_min()

            if in_mst[node.value]:
                continue

            in_mst[node.value] = True

            for neighbor in self.graph.neighbors(node.value):
                weight = self.graph[node.value][neighbor]["weight"]

                if in_mst[neighbor] is False and key[neighbor] > weight:
                    key[neighbor] = weight
                    queue.insert(key[neighbor], neighbor)
                    mst[neighbor] = node.value

        return mst

    def draw(self, mst: dict[int, int]) -> None:
        for n1 in list(mst.keys()):
            n2 = mst[n1]

            if n1 == -1 or n2 == -1:
                continue

            self.graph[n1][n2]['color'] = 'red'

        GraphVisualizer(self.graph).\
            withNodeColor(self.start_node, 'red').\
            withEdgeColors().\
            draw().\
            withWeight().\
            show()
