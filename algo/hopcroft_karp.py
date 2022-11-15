import math
from networkx import Graph

from algorithm import AlgoContext, AlgoResult


def HopcroftKarpDFS(
        context: AlgoContext,
        node: int,
        matching: dict[Graph.nodes, Graph.nodes],
        distance: dict[Graph.nodes, int | float]
) -> bool:
    if node != -1:
        for neighbour in context.graph.neighbors(node):
            if distance[matching[neighbour]] == distance[node] + 1 \
                    and HopcroftKarpDFS(context, matching[neighbour], matching, distance):

                matching[neighbour] = node
                matching[node] = neighbour

                return True

        distance[node] = math.inf
        return False

    return True


def HopcroftKarpBFS(
        context: AlgoContext,
        matching: dict[Graph.nodes, Graph.nodes],
        distance: dict[Graph.nodes, int | float]
) -> bool:
    queue = []

    for node in context.graph.nodes:
        if matching[node] == -1:
            distance[node] = 0
            queue.append(node)
        else:
            distance[node] = math.inf

    distance[-1] = math.inf

    while queue:
        node = queue.pop(0)

        if node != -1 and distance[node] < math.inf:
            for neighbour in context.graph.neighbors(node):
                if distance[matching[neighbour]] == math.inf:
                    distance[matching[neighbour]] = distance[node] + 1
                    queue.append(matching[neighbour])

    return distance[-1] != math.inf


def HopcroftKarp(context: AlgoContext) -> AlgoResult:
    matching = {}
    distance = {}

    for node in context.graph.nodes:
        distance[node] = 0
        matching[node] = -1

    while HopcroftKarpBFS(context, matching, distance):
        for node in context.graph.nodes:
            if matching[node] == -1:
                HopcroftKarpDFS(context, node, matching, distance)

    edges = []
    for u, v in matching.items():
        edges.append((u, v))

    return AlgoResult(context).withEdgeColors(edges)
