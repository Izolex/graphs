from __future__ import annotations
from fibonacci import *
from visualizer import *


class Kruskal:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph, start_node: int) -> None:
        self.graph = graph
        self.start_node = start_node

    def __find(self, forest, i):
        if forest[i] == i:
            return i
        return self.__find(forest, forest[i])

    def __union(self, forest, rank, x, y):
        x_set = self.__find(forest, x)
        y_set = self.__find(forest, y)

        if rank[x_set] < rank[y_set]:
            forest[x_set] = y_set
        elif rank[x_set] > rank[y_set]:
            forest[y_set] = x_set
        else:
            forest[y_set] = x_set
            rank[x_set] += 1

    def run(self) -> list[graph.edges]:
        mst = []
        forest = []
        rank = []

        queue = FibonacciHeap()

        for node in self.graph.nodes:
            forest.append(node)
            rank.append(0)

        for edge in self.graph.edges:
            weight = self.graph[edge[0]][edge[1]]['weight']
            queue.insert(weight, edge)

        while not queue.is_empty():
            node = queue.extract_min()
            edge = node.value

            x = self.__find(forest, edge[0])
            y = self.__find(forest, edge[1])
            if x != y:
                mst.append(edge)
                self.__union(forest, rank, x, y)

        return mst

    def draw(self, mst: list[graph.edges]) -> None:
        for edge in mst:
            self.graph[edge[0]][edge[1]]['color'] = 'red'

        GraphVisualizer(self.graph).\
            withNodeColor(self.start_node, 'red').\
            withEdgeColors().\
            draw().\
            withWeight().\
            show()
