from __future__ import annotations

import math
from networkx import Graph

from algorithm import AlgoContext
from data_struct.fibonacci import FibonacciHeap


def Dijkstra(context: AlgoContext) -> dict[Graph.nodes, int]:
    distances = {v: math.inf for v in context.graph.nodes.keys()}
    distances[context.start_node] = 0

    visited = {}

    queue = FibonacciHeap()
    queue.insert(0, context.start_node)

    while not queue.is_empty():
        node = queue.extract_min()
        visited[node.value] = 0

        for neighbor in context.graph.neighbors(node.value):
            weight = context.graph[node.value][neighbor]["weight"]

            if neighbor not in visited:
                cost = distances[node.value] + weight
                if cost < distances[neighbor]:
                    queue.insert(cost, neighbor)
                    distances[neighbor] = cost

    return distances
