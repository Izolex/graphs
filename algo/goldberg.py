from numpy import Inf

from algorithm import *


class GoldBergAlgo:
    context: AlgoContext
    flow: dict[Graph.edges, int]
    height: list[int]
    overflow: list[int]

    def __init__(self, context: AlgoContext):
        self.context = context

        self.flow = {}
        for edge in context.graph.edges:
            self.flow[edge] = self.flow[tuple(reversed(edge))] = 0

        nodes_count = len(list(context.graph.nodes))

        self.height = [0] * nodes_count
        self.height[context.start_node] = nodes_count

        self.overflow = [0] * nodes_count
        self.overflow[context.start_node] = Inf

    def push(self, u, v):
        capacity = self.context.graph[u][v]['weight']

        send = min(self.overflow[u], capacity - self.flow[(u, v)])
        self.flow[(u, v)] += send
        self.flow[(v, u)] -= send
        self.overflow[u] -= send
        self.overflow[v] += send

    def relabel(self, node: int):
        minimum = float('inf')
        for neighbour in self.context.graph.neighbors(node):
            capacity = self.context.graph[node][neighbour]['weight']
            if capacity - self.flow[(node, neighbour)] > 0:
                minimum = min(minimum, self.height[neighbour])
                self.height[node] = minimum + 1

    def discharge(self, node: int):
        while self.overflow[node] > 0:
            for neighbour in self.context.graph.neighbors(node):
                capacity = self.context.graph[node][neighbour]['weight']
                if capacity - self.flow[(node, neighbour)] > 0 and self.height[node] > self.height[neighbour]:
                    self.push(node, neighbour)

            self.relabel(node)

    def run(self) -> dict[Graph.edges, int]:
        for neighbour in self.context.graph.neighbors(self.context.start_node):
            self.push(self.context.start_node, neighbour)

        nodes = []
        for n in self.context.graph.nodes:
            if n != self.context.start_node and n != self.context.end_node:
                nodes.append(n)

        i = 0
        while i < len(nodes):
            node = nodes[i]
            height = self.height[node]
            self.discharge(node)

            if self.height[node] > height:
                nodes.insert(0, nodes.pop(i))
                i = 0
            else:
                i += 1

        return self.flow


def Goldberg(context: AlgoContext) -> dict[Graph.edges, int]:
    return GoldBergAlgo(context).run()
