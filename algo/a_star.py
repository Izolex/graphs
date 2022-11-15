import networkx

from algorithm import *
from data_struct.fibonacci import FibonacciHeap


def graphDistance(context: AlgoContext, n1: int, n2: int) -> float:
    if n1 == n2:
        return 0

    return networkx.resistance_distance(context.graph, n1, n2)


def AStar(context: AlgoContext) -> list[Graph.edges]:
    source = {}

    distances = {context.start_node: graphDistance(context, context.start_node, context.end_node)}

    queue = FibonacciHeap()
    queue.insert(0, context.start_node)

    while not queue.is_empty():
        node = queue.extract_min().value

        if node == context.end_node:
            break

        for neighbour in context.graph.neighbors(node):
            cost = distances[node] + graphDistance(context, node, neighbour)

            if neighbour not in distances or cost < distances[neighbour]:
                distances[neighbour] = cost
                source[neighbour] = node

                end_cost = graphDistance(context, neighbour, context.end_node)
                priority = cost + end_cost
                queue.insert(priority, neighbour)

    path = []

    for u, v in source.items():
        path.append((v, u))

    return path
