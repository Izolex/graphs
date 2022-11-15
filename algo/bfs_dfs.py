from algorithm import *


def bfs_dfs_algo(context: AlgoContext, obtain_func) -> AlgoResult:
    queue = [context.start_node]

    visited = {context.start_node: 1}
    iterator = 2

    while queue:
        node = obtain_func(queue)

        for neighbour in context.graph.neighbors(node):
            if neighbour not in visited:

                visited[neighbour] = iterator
                iterator += 1
                queue.append(neighbour)

    return AlgoResult(context).withNodeLabels(visited).withStartColor()


def BFS(context: AlgoContext) -> AlgoResult:
    return bfs_dfs_algo(context, lambda l: l.pop(0))


def DFS(context: AlgoContext) -> AlgoResult:
    return bfs_dfs_algo(context, lambda l: l.pop(-1))
