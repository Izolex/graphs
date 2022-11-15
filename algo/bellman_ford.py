from __future__ import annotations

import math
from networkx import Graph

from algorithm import AlgoContext


def BellmanFord(context: AlgoContext) -> dict[Graph.nodes, int]:
    distances = {v: math.inf for v in context.graph.nodes.keys()}
    distances[context.start_node] = 0

    for _ in range(len(context.graph.nodes) - 1):
        for edge in context.graph.edges:
            weight = context.graph[edge[0]][edge[1]]["weight"]
            if distances[edge[0]] != math.inf and distances[edge[0]] + weight < distances[edge[1]]:
                distances[edge[1]] = distances[edge[0]] + weight

    return distances
