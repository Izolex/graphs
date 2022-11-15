import math

from algorithm import AlgoContext


def DinicBFS(context: AlgoContext, flow):
    queue = [context.start_node]

    level = [0] * len(list(context.graph.nodes))
    level[context.start_node] = 1

    while queue:
        node = queue.pop(0)

        for neighbour in context.graph.neighbors(node):
            capacity = context.graph[node][neighbour]['weight']

            if level[neighbour] == 0 and flow[(node, neighbour)] < capacity:
                level[neighbour] = level[node] + 1
                queue.append(neighbour)

    return level


def DinicDFS(context: AlgoContext, start, level, flow, max_flow):
    temp_flow = max_flow

    if start == context.end_node:
        return max_flow

    for node in context.graph.neighbors(start):
        if level[node] != level[start] + 1:
            continue

        capacity = context.graph[start][node]['weight']
        current = flow[(start, node)]

        if current < capacity:
            m = min(temp_flow, capacity - current)
            node_flow = DinicDFS(context, node, level, flow, m)

            flow[(start, node)] = flow[(start, node)] + node_flow
            flow[(node, start)] = flow[(node, start)] - node_flow

            temp_flow = temp_flow - node_flow

    return max_flow - temp_flow


def Dinic(context: AlgoContext):
    flow = {}
    for edge in context.graph.edges:
        flow[edge] = flow[tuple(reversed(edge))] = 0

    while level := DinicBFS(context, flow):
        if level[context.end_node] == 0:
            break

        DinicDFS(context, context.start_node, level, flow, math.inf)

    return flow
