# KruskalMST(G):
#  DisjointSets forest
#  foreach (Vertex v : G):
#  forest.makeSet(v)
#  PriorityQueue Q // min edge weight
#  foreach (Edge e : G):
#  Q.insert(e)
#  Graph T = (V, {})
#
#  while |T.edges()| < n-1:
#  Vertex (u, v) = Q.removeMin()
#  if forest.find(u) != forest.find(v):
#  T.addEdge(u, v)
#  forest.union( forest.find(u),
#  forest.find(v) )
#  return T

from __future__ import annotations
from fibonacci import *
from visualizer import *


class Kruskal:
    graph: Graph
    start_node: int

    def __init__(self, graph: Graph, start_node: int) -> None:
        self.graph = graph
        self.start_node = start_node

    def __makeSet(self, parent, universe):
        # create `n` disjoint sets (one for each item)
        for i in universe:
            parent[i] = i

    def __find(self, parent, i):
        if parent[i] == i:
            return i
        return self.__find(parent, parent[i])

    def __union(self, parent, a, b):
        # find the root of the sets in which elements
        # `x` and `y` belongs
        x = self.__find(parent, a)
        y = self.__find(parent, b)

        parent[x] = y

    def run(self) -> dict[int, int]:
        forest = {}

        queue = FibonacciHeap()

        for edge in self.graph.edges:
            forest[edge[0]] = edge[0]
            forest[edge[1]] = edge[1]
            queue.insert(self.graph[edge[0]][edge[1]]['weight'], edge)

        mst = {}

        while not queue.is_empty():
            node = queue.extract_min()
            edge = node.value

            x = self.__find(forest, edge[0])
            y = self.__find(forest, edge[1])
            if x != y:
                mst[edge[1]] = edge[0]
                self.__union(forest, x, y)

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
