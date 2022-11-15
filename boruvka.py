from __future__ import annotations
from visualizer import *


class Boruvka:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

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

        nodes_dec = nodes_len = len(self.graph.nodes)
        cheapest = [-1] * nodes_len

        for node in self.graph.nodes:
            forest.append(node)
            rank.append(0)

        while nodes_dec > 1:
            for edge in self.graph.edges:
                w = self.graph[edge[0]][edge[1]]["weight"]
                x = self.__find(forest, edge[0])
                y = self.__find(forest, edge[1])

                if x != y:
                    if cheapest[x] == -1 or cheapest[x][2] > w:
                        cheapest[x] = (edge[0], edge[1], w)

                    if cheapest[y] == -1 or cheapest[y][2] > w:
                        cheapest[y] = (edge[0], edge[1], w)

            for node in self.graph.nodes:
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    x_set = self.__find(forest, u)
                    y_set = self.__find(forest, v)

                    if x_set != y_set:
                        mst.append((u, v))
                        self.__union(forest, rank, x_set, y_set)
                        nodes_dec = nodes_dec - 1

            cheapest = [-1] * nodes_len

        return mst

    def draw(self, mst: list[graph.edges]) -> None:
        for edge in mst:
            self.graph[edge[0]][edge[1]]['color'] = 'red'

        GraphVisualizer(self.graph).\
            withEdgeColors().\
            draw().\
            withWeight().\
            show()
