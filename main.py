from dijkstra import *
from prim import *
from kruskal import *
from fibonacci import *
from welsh_powell import *
from dsatur import *

nodes = [
    0, 1, 2,
    3, 4, 5,
]

edges = [
    (0, 1, 10),
    (0, 3, 20),
    (0, 4, 30),

    (3, 4, 90),
    (3, 6, 80),

    (1, 2, 70),
    (1, 4, 60),
    (1, 5, 40),

    (4, 5, 50),
]

# nodes = [0, 1, 2, 3, 4, 5]
# edges = [(0, 2, 1), (1, 3, 2), (3, 4, 3), (2, 3, 4), (2, 5, 5), (1, 3, 6), (3, 1, 7), (4, 5, 10)]

graph = networkx.Graph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)

algo = "fibonacci"
algo = "dijkstra"
algo = "prim"
algo = "kruskal"
algo = "welsh_powell"
algo = "dsatur"

match algo:
    case "fibonacci":
        fib_nodes = [Node(i, 0) for i in range(1, 20)]

        h = FibonacciHeap()

        for n in fib_nodes:
            h.merge(n)

        h.print()
        h.extract_min()
        h.print()
        h.decrease_key(fib_nodes[5], 1)
        h.print()
        GraphVisualizer(h.get_graph()).draw().show()

    case "dijkstra":
        dij = Dijkstra(graph, nodes[0])
        dij.draw(dij.run())

    case "prim":
        pri = Prim(graph, nodes[0])
        pri.draw(pri.run())

    case "kruskal":
        kru = Kruskal(graph, nodes[0])
        kru.draw(kru.run())

    case "welsh_powell":
        wp = WelshPowell(graph)
        wp.draw(wp.run())

    case "dsatur":
        wp = DSatur(graph)
        wp.draw(wp.run())

    case _:
        print("wtf")
