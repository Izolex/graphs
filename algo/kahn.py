from algorithm import *


def getOutwardsEdges(context: AlgoContext, node: int):
    edges = []

    for neighbour in context.graph.neighbors(node):
        if (node, neighbour) in list(context.graph.edges):
            edges.append(neighbour)

    return edges


def Kahn(context: AlgoContext) -> AlgoResult:
    degree = [0] * len(list(context.graph.nodes))

    for node in context.graph.nodes:
        for neighbour in getOutwardsEdges(context, node):
            degree[neighbour] += 1

    queue = []
    for node in context.graph.nodes:
        if degree[node] == 0:
            queue.append(node)

    count = 0
    order = {}
    while queue:
        node = queue.pop(0)
        order[node] = count

        for neighbour in getOutwardsEdges(context, node):
            degree[neighbour] -= 1
            if degree[neighbour] == 0:
                queue.append(neighbour)

        count += 1

    if count != len(list(context.graph.nodes)):
        raise Exception("ups some cycle :/")

    return AlgoResult(context).withNodeLabels(order)
