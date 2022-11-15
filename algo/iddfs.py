from typing import Optional

from algorithm import *


def search(context: AlgoContext, path: list[Graph.nodes], depth: int) -> Optional[list[Graph.nodes]]:
    node = path[-1]

    if context.end_node == node:
        return path
    if depth <= 0:
        return None

    neighbours = list(context.graph.neighbors(node))
    neighbours.sort(key=lambda n: context.graph[node][n]['weight'])

    for neighbour in neighbours:
        new_path = list(path)
        new_path.append(neighbour)
        result_path = search(context, new_path, depth - 1)

        if result_path is not None:
            return result_path


def IDDFS(context: AlgoContext) -> AlgoResult:
    depth = 1
    while True:
        path = [context.start_node]
        result = search(context, path, depth)

        if result is None:
            depth += 1
            continue

        mst = []
        for idx, node in enumerate(result[1:]):
            mst.append((result[idx], node))

        return AlgoResult(context).\
            withEdgeColors(mst).\
            withWeights().\
            withStartColor().\
            withEndColor()
