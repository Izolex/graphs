from __future__ import annotations
from fibonacci import *
from algorithm import *


def Prim(context: AlgoContext) -> list[Graph.edges]:
    key = {v: float('inf') for v in context.graph.nodes.keys()}
    key[context.start_node] = 0

    mst = []
    in_mst = {v: False for v in context.graph.nodes.keys()}

    queue = FibonacciHeap()
    queue.insert(0, context.start_node)
    key[context.start_node] = 0

    while not queue.is_empty():
        node = queue.extract_min()

        if in_mst[node.value]:
            continue

        in_mst[node.value] = True

        for neighbor in context.graph.neighbors(node.value):
            weight = context.graph[node.value][neighbor]["weight"]

            if in_mst[neighbor] is False and key[neighbor] > weight:
                key[neighbor] = weight
                queue.insert(key[neighbor], neighbor)
                mst.append((neighbor, node.value))

    return mst
