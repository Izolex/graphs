from __future__ import annotations

from algorithm import AlgoContext, AlgoResult


def WelshPowell(context: AlgoContext) -> AlgoResult:
    result = {}

    color = -1
    while len(result.items()) < len(context.graph.nodes):
        color += 1
        for node in context.graph.nodes:
            has_neighbour = False
            for neighbor in context.graph.neighbors(node):
                if neighbor in result and result[neighbor] == color:
                    has_neighbour = True
                    break

            if node not in result and not has_neighbour:
                result[node] = color

    return AlgoResult(context).withNodeColors([n[1] for n in sorted(result.items())])
