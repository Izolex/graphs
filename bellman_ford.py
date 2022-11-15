from __future__ import annotations
from visualizer import *


def BellmanFord(context: AlgoContext) -> dict[Graph.nodes, float]:
    distances = {v: float('inf') for v in context.graph.nodes.keys()}
    distances[context.start_node] = 0

    for _ in range(len(context.graph.nodes) - 1):
        for edge in context.graph.edges:
            weight = context.graph[edge[0]][edge[1]]["weight"]
            if distances[edge[0]] != float("Inf") and distances[edge[0]] + weight < distances[edge[1]]:
                distances[edge[1]] = distances[edge[0]] + weight

    return distances
