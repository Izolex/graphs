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
from algo.iddfs import *
from algo.a_star import *
from algo.goldberg import *
from algo.kahn import *
from algo.hopcroft_karp import *
from visualizer import *

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

# edges = [
#     (5, 2, 0),
#     (5, 0, 0),
#     (4, 0, 0),
#     (4, 1, 0),
#     (2, 3, 0),
#     (3, 1, 0),
# ]

# bipartite graph
# edges = [
#     (1, 5, 0),
#     (1, 7, 0),
#     (2, 7, 0),
#     (3, 8, 0),
#     (4, 6, 0),
#     (4, 7, 0),
# ]

# nodes = [0, 1, 2, 3, 4, 5]
# edges = [(0, 2, 1), (1, 3, 2), (3, 4, 3), (2, 3, 4), (2, 5, 5), (1, 3, 6), (3, 1, 7), (4, 5, 10)]


class AlgorithmType(Enum):
    Traversal = "traversal"
    MinimalSpanningTree = "minimalSpanningTree"
    ShortestPath = "shortestPath"
    Coloring = "coloring"
    NetworkFlow = "network_flow"
    MaximumMatching = "maximum_matching"
    Miscellaneous = "miscellaneous"


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
    IDDFS = 'iddfs'
    AStar = 'astar'
    Goldberg = 'goldberg'
    Kahn = 'kahn'
    HopcroftKarp = 'hopcroft_karp'


algorithms = {
    AlgorithmType.Miscellaneous: {
        Algorithm.Kahn: Kahn
    },
    AlgorithmType.Traversal: {
        Algorithm.BFS: BFS,
        Algorithm.DFS: DFS,
        Algorithm.IDDFS: IDDFS,
        Algorithm.AStar: AStar,
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
    AlgorithmType.MaximumMatching: {
        Algorithm.HopcroftKarp: HopcroftKarp,
    },
    AlgorithmType.NetworkFlow: {
        Algorithm.EdmondsKarp: EdmondsKarp,
        Algorithm.Dinic: Dinic,
        Algorithm.Goldberg: Goldberg,
    }
}


def findAlgoType(an: str) -> AlgorithmType:
    for t in algorithms.keys():
        for n in algorithms[t].keys():
            if n.value == an:
                return t

    raise Exception('Algo not found')


name = 'goldberg'

algoType = findAlgoType(name)
algoName = Algorithm(name)

if algoName == Algorithm.Kahn:
    graph = networkx.DiGraph()
else:
    graph = networkx.Graph()

graph.add_weighted_edges_from(edges)
context = AlgoContext(graph, 1, 5)

result = algorithms[algoType][algoName](context)

visualizer = Visualizer(context, result)
visualizer.draw().show()
