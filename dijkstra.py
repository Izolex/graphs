from __future__ import annotations
from fibonacci import *
from visualizer import *


class DijkstraAlgorithm:
    graph: Graph
    start_node: int

    def __init__(self, nodes: list, edges: list[Tuple[int, int, int]], start_node: int) -> None:
        g = networkx.Graph()
        g.add_nodes_from(nodes)
        g.add_weighted_edges_from(edges)
        self.graph = g
        self.start_node = start_node

    def run(self) -> dict[int, int]:
        distances = {v: float('inf') for v in self.graph.nodes.keys()}
        distances[self.start_node] = 0

        visited = {}

        queue = FibonacciHeap()
        queue.insert(0, self.start_node)

        while not queue.is_empty():
            node = queue.extract_min()
            visited[node.value] = 0

            for neighbor in self.graph.neighbors(node.value):
                dis = self.graph[node.value][neighbor]["weight"]

                if neighbor not in visited:
                    old_cost = distances[neighbor]
                    new_cost = distances[node.value] + dis
                    if new_cost < old_cost:
                        queue.insert(new_cost, neighbor)
                        distances[neighbor] = new_cost

        return distances

    def draw(self, distances: dict) -> None:
        colors = ["lightblue"] * len(self.graph.nodes)
        colors[self.start_node] = "red"

        node_labels = {node: str(node) + " (" + str(distances[node]) + ")" for node in distances}
        edge_labels = networkx.get_edge_attributes(self.graph, 'weight')

        vis = GraphVisualizer(self.graph)
        vis.withColors(colors).withNodeLabels(node_labels).draw().withEdgeLabels(edge_labels).show()
