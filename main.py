from enum import Enum
from dijkstra import *
from prim import *
from kruskal import *
from welsh_powell import *
from dsatur import *
from floyd_warshall import *
from bellman_ford import *
from boruvka import *
from rlf import *
from edmonds_karp import *

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


context = AlgoContext(graph, nodes[0], nodes[5])
drawer = GraphDrawer(context)


class AlgorithmType(Enum):
    MinimalSpanningTree = "minimalSpanningTree"
    ShortestPath = "shortestPath"
    Coloring = "coloring"
    NetworkFlow = "network_flow"


class Algorithm(Enum):
    Dijkstra = 'dijkstra'
    FloydWarshall = 'floyd_warshall'
    BellmanFord = 'bellman_ford'
    Kruskal = 'kruskal'
    Prim = 'prim'
    Boruvka = 'boruvka'
    WelshPowell = 'welsh_powell'
    RecursiveLargestFirst = 'rlf'
    DegreeOfSaturation = 'dsatur'
    EdmondsKarp = 'edmonds_karp'


algorithms = {
    AlgorithmType.ShortestPath: {
        Algorithm.Dijkstra: Dijkstra,
        Algorithm.FloydWarshall: FloydWarshall,
        Algorithm.BellmanFord: BellmanFord,
    },
    AlgorithmType.MinimalSpanningTree: {
        Algorithm.Prim: Prim,
        Algorithm.Kruskal: Kruskal,
        Algorithm.Boruvka: Boruvka,
    },
    AlgorithmType.Coloring: {
        Algorithm.WelshPowell: WelshPowell,
        Algorithm.RecursiveLargestFirst: RLF,
        Algorithm.DegreeOfSaturation: DSatur,
    },
    AlgorithmType.NetworkFlow: {
        Algorithm.EdmondsKarp: EdmondsKarp,
    }
}


def findAlgoType(an: str) -> AlgorithmType:
    for t in algorithms.keys():
        for n in algorithms[t].keys():
            if n.value == an:
                return t

    raise Exception('Algo not found')


name = 'edmonds_karp'
algoType = findAlgoType(name)
algoName = Algorithm(name)
result = algorithms[algoType][algoName](context)

match algoType:
    case AlgorithmType.MinimalSpanningTree:
        drawer.minimalSpanningTree(result)
    case AlgorithmType.ShortestPath:
        drawer.shortestPath(result)
    case AlgorithmType.Coloring:
        drawer.coloring(result)
    case AlgorithmType.NetworkFlow:
        drawer.networkFlow(result)
