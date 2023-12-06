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

class QNode:
    _id_counter = count()
    def __init__(self, x: float, y: float, h=0, label=""):
        self.x = x
        self.y = y
        self.h = h
        self.label = label
        self.id = next(self._id_counter) # TODO: remove if not needed

class ENode:
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

    def add_q_node(self, n1,n2,n3,n4):
        node = QNode(
            x = (n1.x + n2.x + n3.x + n4.x) / 4,
            y = (n1.y + n2.y + n3.y + n4.y) / 4,
            label = "Q"
        )
        self.G.add_node(node)
        self.add_hyperedge(n1, node)
        self.add_hyperedge(n2, node)
        self.add_hyperedge(n3, node)
        self.add_hyperedge(n4, node)
        return node

    def add_hyperedge(self, v1: QNode, v2: QNode):
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")
        self.G.add_edge(v1, v2)

    def add_edge(self, v1: Node, v2: Node, B=0, R=0):
        node = ENode(
            x = (v1.x + v2.x) / 2,
            y = (v1.y + v2.y) / 2,
            label = "E"
        )
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")

        self.G.add_edge(v1, v2, B=B, R=R)
        self.G.add_node(node)
        return node

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
        labels = {node: node.label + " " + str(node.id) for node in self.G.nodes}
        color_map = []
        for node in self.G:
            if node.label == "Q":
                color_map.append('lightgreen')
            elif node.label == "E":
                color_map.append("lightgrey")
            else:
                color_map.append('lightblue')
        nx.draw(self.G, pos=pos, with_labels=True, labels=labels, node_color=color_map, node_size=400, font_size=10,
                edge_color='gray')
        plt.show()




