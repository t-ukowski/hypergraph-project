from itertools import count
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


class Node:
    _id_counter = count()

    def __init__(self, x: float, y: float, h=0, label=""):
        self.x = x
        self.y = y
        self.h = h
        self.label = label
        self.id = next(self._id_counter) # TODO: remove if not needed

# TODO: B and R should be int or boolean ?
class Edge:
    def __init__(self, v1: Node, v2: Node, B=0, R=0):
        self.v1 = v1
        self.v2 = v2
        self.B = B
        self.R = R

class Graph:
    def __init__(self):
        self.G = nx.Graph()

    def __contains__(self, node):
        return self.has_node(node)

    def has_node(self, node: Node):
        return node in self.G

    def add_node(self, node: Node):
        self.G.add_node(node, node=node)

    def add_edge(self, v1: Node, v2: Node, B=0, R=0):
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")

        self.G.add_edge(v1, v2, B=B, R=R)

    def get_nodes(self):
        return self.G.nodes

    def get_number_of_nodes(self):
        return self.G.number_of_nodes()

    def get_edges(self):
        return self.G.edges(data=True)

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
        nx.draw(self.G, pos, with_labels=True, labels=labels, node_color='lightblue', node_size=400, font_size=10,
                edge_color='gray')
        plt.show()



