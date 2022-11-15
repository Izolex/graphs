from dijkstra import *
from fibonacci import *

nodes = [0, 1, 2, 3, 4, 5]
edges = [(0, 2, 1), (1, 3, 2), (3, 4, 3), (2, 3, 4), (2, 5, 5), (1, 3, 6), (3, 1, 7)]

dij = DijkstraAlgorithm(nodes, edges, nodes[0])
distances = dij.run()
dij.draw(distances)

nodes = [Node(i, 0) for i in range(1, 20)]

h = FibonacciHeap()

for n in nodes:
    h.merge(n)

h.print()

h.extract_min()

h.print()

h.decrease_key(nodes[5], 1)

h.print()

vis = GraphVisualizer(h.get_graph())
