from __future__ import annotations

import math
import numpy
from networkx import Graph

from algorithm import AlgoContext


def FloydWarshall(context: AlgoContext) -> dict[Graph.nodes, int]:
    edges_len = len(context.graph.edges)

    dist = numpy.full((edges_len, edges_len), math.inf, float)

    for edge in context.graph.edges:
        dist[edge[0]][edge[1]] = context.graph[edge[0]][edge[1]]['weight']

    for node in context.graph.nodes:
        dist[node][node] = 0

    for k in range(edges_len):
        for i in range(edges_len):
            for j in range(edges_len):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return {n: dist[context.start_node][n] for n in context.graph.nodes}
