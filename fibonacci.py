from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator, Optional, Tuple
import networkx
from networkx import Graph


@dataclass
class Node:
    key: int
    value: int
    rank: Optional[int] = 0
    mark: Optional[bool] = False
    parent: Optional[Node] = None
    child: Optional[Node] = None
    left: Optional[Node] = None
    right: Optional[Node] = None

    def __post_init__(self):
        if self.left is None:
            self.left = self
        if self.right is None:
            self.right = self


class FibonacciHeap:
    root: Node | None = None
    rank: int = 0

    def __unlink(self, node: Node) -> None:
        node.left.right = node.right
        node.right.left = node.left

    def __iterate(self, mini: Node) -> Iterator[Node]:
        node = mini

        while True:
            yield node
            node = node.right
            if node == mini:
                return

    def __find_neighbours(self, mini: Node, node: Node) -> Tuple[Node, Node]:
        n = mini
        while node.key < n.key and n != mini:
            n = n.right

        return n.left, n

    def __insert_child(self, parent: Node, child: Node) -> None:
        parent.rank += 1

        if parent.child is None:
            parent.child = child
            child.parent = parent
            child.left = child
            child.right = child
            return

        left, right = self.__find_neighbours(parent.child, child)

        if child.key < parent.child.key:
            parent.child = child

        child.parent = parent
        if left == right:
            if left.key < child.key:
                left.right = child
                left.left = child
                child.left = left
                child.right = left
            else:
                left.left = child
                left.right = child
                child.right = left
                child.left = left
        else:
            child.left = left
            child.right = right
            left.right = child
            right.left = child

    def __insert_sibling(self, a: Node, b: Node) -> None:
        left, right = self.__find_neighbours(a, b)

        if a.parent is not None and a.parent.key > b.key:
            a.parent.child = b
        b.parent = a.parent

        if left == right:
            left.right = b
            left.left = b
            b.right = left
            b.left = left
        else:
            b.left = left
            b.right = right
            left.right = b
            right.left = b

    def __consolidate(self) -> None:
        if self.rank == 0:
            self.root = None
            return

        nodes = [n for n in self.__iterate(self.root)]
        ranks: list[Node | None] = [None] * self.rank

        for node in nodes:
            rank = node.rank

            while ranks[node.rank] is not None:
                self.rank -= 1

                if node.key > ranks[node.rank].key:
                    self.__unlink(node)
                    self.__insert_child(ranks[node.rank], node)
                    node = ranks[node.rank]
                else:
                    self.__unlink(ranks[node.rank])
                    self.__insert_child(node, ranks[node.rank])

                ranks[rank] = None
                rank = node.rank

            ranks[rank] = node

        for node in nodes:
            if node is not None and node.key < self.root.key:
                self.root = node

    def extract_min(self) -> Node:
        mini = self.root
        self.__unlink(mini)
        self.root = mini.right
        self.rank -= 1

        n = mini.child
        if n is not None:
            while n is not mini.child:
                r = n.right
                self.merge(n)
                n = r

        self.__consolidate()

        return mini

    def __rooted_cut(self, node: Node) -> None:
        node.parent.rank -= 1

        if node.parent.child == node:
            if node.right == node:
                node.parent.child = None
            else:
                node.parent.child = node.right

        self.__unlink(node)
        self.merge(node)

    def __recursive_cut(self, node: Node) -> None:
        if node.parent is not None:
            if not node.parent.mark:
                node.parent.mark = True
            else:
                self.__rooted_cut(node)
                self.__recursive_cut(node.parent)

    def decrease_key(self, node: Node, new_key: int) -> None:
        node.key = new_key

        if node.parent.key < new_key:
            if node.parent.child.key > new_key:
                node.parent.child = node

            return

        parent = node.parent
        node.mark = False

        if parent is not None:
            parent.mark = True
            self.__rooted_cut(node)
            self.__recursive_cut(parent)

        if node.key < self.root.key:
            self.root = node

    def merge(self, node: Node | FibonacciHeap) -> None:
        if isinstance(node, FibonacciHeap):
            for n in node.__iterate(node.root):
                self.merge(n)
        else:
            self.rank += 1
            node.parent = None

            if self.root is None:
                self.root = node
                return

            self.__insert_sibling(self.root, node)
            if node.key < self.root.key:
                self.root = node

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, key: int, value: int) -> None:
        self.merge(Node(key, value))

    def __get_nodes_edges(self, node: Node) -> Tuple[list[int], list[dict]]:
        nodes = []
        edges = []
        for n in self.__iterate(node):
            edges.append((n.left.key, n.key))
            edges.append((n.right.key, n.key))
            nodes.append(n.key)

            if n.parent is not None:
                edges.append((n.parent.key, n.key))

            if n.rank and n.child:
                n2, e2 = self.__get_nodes_edges(n.child)
                nodes.extend(n2)
                edges.extend(e2)
                edges.append((n.child.key, n.key))

        return nodes, edges

    def get_graph(self) -> Graph:
        nodes, edges = self.__get_nodes_edges(self.root)
        g = networkx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)

        return g

    def __printNode(self, level: int, node: Node) -> None:
        mini = node

        for node in self.__iterate(mini):
            print(
                "-" * level,
                " k:",
                node.key,
                " r:",
                node.rank,
                " m:",
                node.child.key if node.child is not None else 0,
                " l:",
                node.left.key if node.left is not None else 0,
                " r:",
                node.right.key if node.right is not None else 0
            )

            if node.child is not None:
                self.__printNode(level + 1, node.child)

    def print(self) -> None:
        print("HEAP:")
        print("min: ", self.root.key, " rank: ", self.rank)
        self.__printNode(1, self.root)
