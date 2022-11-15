from __future__ import annotations

from networkx import Graph

from data_struct.fibonacci import FibonacciHeap
from data_struct.disjoint_set import DisjointSet
from algorithm import AlgoContext, AlgoResult


def Kruskal(context: AlgoContext) -> AlgoResult:
    mst = []
    forest = DisjointSet()

    queue = FibonacciHeap()

    for node in context.graph.nodes:
        forest.append(node)

    for edge in context.graph.edges:
        weight = context.graph[edge[0]][edge[1]]['weight']
        queue.insert(weight, edge)

    while not queue.is_empty():
        node = queue.extract_min()
        edge = node.value

        x = forest.find(edge[0])
        y = forest.find(edge[1])
        if x != y:
            mst.append(edge)
            forest.union(x, y)

    return AlgoResult(context).withWeights().withEdgeColors(mst)
