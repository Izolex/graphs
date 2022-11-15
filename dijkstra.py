from __future__ import annotations
from fibonacci import *
from algorithm import *


def Dijkstra(context: AlgoContext) -> dict[Graph.nodes, float]:
    distances = {v: float('inf') for v in context.graph.nodes.keys()}
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
