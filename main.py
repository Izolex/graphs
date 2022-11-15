from enum import Enum

import networkx

from algo.bfs_dfs import *
from algo.dijkstra import *
from algo.prim import *
from algo.kruskal import *
from algo.welsh_powell import *
from algo.dsatur import *
from algo.floyd_warshall import *
from algo.bellman_ford import *
from algo.boruvka import *
from algo.rlf import *
from algo.edmonds_karp import *
from algo.dinic import *
from visualization import *

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
    Traversal = "traversal"
    MinimalSpanningTree = "minimalSpanningTree"
    ShortestPath = "shortestPath"
    Coloring = "coloring"
    NetworkFlow = "network_flow"


class Algorithm(Enum):
    BFS = 'bfs'
    DFS = 'dfs'
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
    Dinic = 'dinic'


algorithms = {
    AlgorithmType.Traversal: {
        Algorithm.BFS: BFS,
        Algorithm.DFS: DFS,
    },
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
        Algorithm.Dinic: Dinic,
    }
}


def findAlgoType(an: str) -> AlgorithmType:
    for t in algorithms.keys():
        for n in algorithms[t].keys():
            if n.value == an:
                return t

    raise Exception('Algo not found')


name = 'bfs'
algoType = findAlgoType(name)
algoName = Algorithm(name)
result = algorithms[algoType][algoName](context)

match algoType:
    case AlgorithmType.Traversal:
        drawer.traversal(result)
    case AlgorithmType.MinimalSpanningTree:
        drawer.minimalSpanningTree(result)
    case AlgorithmType.ShortestPath:
        drawer.shortestPath(result)
    case AlgorithmType.Coloring:
        drawer.coloring(result)
    case AlgorithmType.NetworkFlow:
        drawer.networkFlow(result)
