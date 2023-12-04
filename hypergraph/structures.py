from itertools import count
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


class Node:
    _id_counter = count()

    def __init__(self, x: float, y: float, h: int, label: str, level: int):
        self.x = x
        self.y = y
        self.h = h
        self.label = label
        self.level = level
        self.id = next(self._id_counter)

class Graph:
    def __init__(self):
        self.G = nx.Graph()

    def __contains__(self, node):
        return self.has_node(node)

    def has_node(self, node: Node):
        return node in self.G

    def add_node(self, node: Node):
        self.G.add_node(node, node=node)

    def add_edge(self, v1: Node, v2: Node):
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")

        self.G.add_edge(v1, v2)

    def get_nodes(self):
        return self.G.nodes

    def get_number_of_nodes(self):
        return self.G.number_of_nodes()

    def get_edges(self):
        return self.G.edges

    def get_number_of_edges(self):
        return self.G.number_of_edges()

    def remove_node(self, node: Node) -> None:
        if node not in self:
            raise ValueError(f"{node} not in graph")
        self.G.remove_node(node)

    def remove_edge(self, v1: Node, v2: Node):
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")

        self.G.remove_edge(v1, v2)

    def visualize(self):
        pos = {node: (node.x, node.y) for node in self.G.nodes}
        labels = {node: node.label for node in self.G.nodes}
        nx.draw(graph.G, pos, with_labels=True, labels=labels, node_color='lightblue', node_size=500, font_size=12,
                edge_color='gray')
        plt.show()





node1 = Node(1, 3, 3, "a")
node2 = Node(1, 1, 1, "b")
node3 = Node(4, 2, 3, "c")

graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)


graph.add_edge(node1, node2)
graph.add_edge(node2, node3)


graph.visualize()