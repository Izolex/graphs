from algorithm import *


def EdmondsKarpBFS(context: AlgoContext, flow):
    queue = [context.start_node]
    paths = {context.start_node: []}

    while queue:
        node = queue.pop()

        for neighbour in context.graph.neighbors(node):
            weight = context.graph[node][neighbour]['weight']
            if weight - flow[(node, neighbour)] > 0 and neighbour not in paths:
                paths[neighbour] = paths[node] + [(node, neighbour)]

                if neighbour == context.end_node:
                    return paths[neighbour]

                queue.append(neighbour)

    return None


def EdmondsKarp(context: AlgoContext):
    flow = {}
    for edge in context.graph.edges:
        flow[edge] = flow[tuple(reversed(edge))] = 0

    while path := EdmondsKarpBFS(context, flow):
        path_flow = min(context.graph[e[0]][e[1]]['weight'] - flow[e] for e in path)

        for e in path:
            flow[e] += path_flow
            flow[tuple(reversed(e))] -= path_flow

    return flow