from __future__ import annotations
from algorithm import *
from disjoint_set import *


def Boruvka(context: AlgoContext) -> list[Graph.edges]:
    mst = []
    forest = DisjointSet()
    rank = []

    nodes_dec = nodes_len = len(context.graph.nodes)
    cheapest = [-1] * nodes_len

    for node in context.graph.nodes:
        forest.append(node)
        rank.append(0)

    while nodes_dec > 1:
        for edge in context.graph.edges:
            w = context.graph[edge[0]][edge[1]]["weight"]
            x = forest.find(edge[0])
            y = forest.find(edge[1])

            if x != y:
                if cheapest[x] == -1 or cheapest[x][2] > w:
                    cheapest[x] = (edge[0], edge[1], w)

                if cheapest[y] == -1 or cheapest[y][2] > w:
                    cheapest[y] = (edge[0], edge[1], w)

        for node in context.graph.nodes:
            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                x_set = forest.find(u)
                y_set = forest.find(v)

                if x_set != y_set:
                    mst.append((u, v))
                    forest.union(x_set, y_set)
                    nodes_dec = nodes_dec - 1

        cheapest = [-1] * nodes_len

    return mst
