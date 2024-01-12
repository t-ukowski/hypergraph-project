import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")


class Node:
    def __init__(self, x: float, y: float, h=0):
        self.x = x
        self.y = y
        self.h = h
        self.label = "V"


class QNode:
    def __init__(self, x: float, y: float, R=0):
        self.x = x
        self.y = y
        self.R = R
        self.label = "Q"


class SNode:
    def __init__(self, x: float, y: float, R=0):
        self.x = x
        self.y = y
        self.R = R
        self.label = "S"


class ENode:
    def __init__(self, x: float, y: float, B=0):
        self.x = x
        self.y = y
        self.B = B
        self.label = "E"


class Edge:
    def __init__(self, v1: Node, v2: Node):
        self.v1 = v1
        self.v2 = v2


class Graph:
    def __init__(self):
        self.G = nx.Graph()
        self.normal_nodes = []

    def __contains__(self, node):
        return self.has_node(node)

    def has_node(self, node):
        return node in self.G

    def add_node(self, node: Node):
        self.normal_nodes.append(node)
        self.G.add_node(node, node=node)

    def add_q_node(self, n1, n2, n3, n4):
        node = QNode(
            x=(n1.x + n2.x + n3.x + n4.x) / 4, y=(n1.y + n2.y + n3.y + n4.y) / 4
        )
        self.G.add_node(node, node=node)
        self.add_hyperedge(n1, node)
        self.add_hyperedge(n2, node)
        self.add_hyperedge(n3, node)
        self.add_hyperedge(n4, node)

        return node

    def add_s_node(self, n1, n2, n3, n4, n5, n6):
        node = SNode(
            x=(n1.x + n2.x + n3.x + n4.x + n5.x + n6.x) / 6,
            y=(n1.y + n2.y + n3.y + n4.y + n5.y + n6.y) / 6,
        )
        self.G.add_node(node, node=node)
        self.add_hyperedge(n1, node)
        self.add_hyperedge(n2, node)
        self.add_hyperedge(n3, node)
        self.add_hyperedge(n4, node)
        self.add_hyperedge(n5, node)
        self.add_hyperedge(n6, node)

        return node

    def add_hyperedge(self, v1, v2):
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")
        self.G.add_edge(v1, v2)

    def remove_q_node(self, v1: QNode):
        self.G.remove_node(v1)

    def add_edge(self, v1: Node, v2: Node):
        node = ENode(x=(v1.x + v2.x) / 2, y=(v1.y + v2.y) / 2)
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")

        self.G.add_node(node, node=node)
        self.G.add_edge(v1, node)
        self.G.add_edge(node, v2)

        return node

    def get_nodes(self):
        return self.G.nodes

    def get_number_of_nodes(self):
        return len(self.normal_nodes)

    def get_edges(self):
        return self.G.edges(data=True)

    def get_number_of_edges(self):
        return self.G.number_of_nodes() - len(self.normal_nodes)

    def remove_node(self, node: Node) -> None:
        if node not in self:
            raise ValueError(f"{node} not in graph")
        self.G.remove_node(node)

    def remove_edge(self, v1: Node, v2: Node, e1: ENode):
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")
        if e1 not in self:
            raise ValueError(f"{e1} not in graph")

        self.G.remove_edge(v1, e1)
        self.G.remove_edge(e1, v2)
        self.G.remove_node(e1)

    def split_edge(self, v1: Node, v2: Node, e1: ENode):
        if v1 not in self:
            raise ValueError(f"{v1} not in graph")
        if v2 not in self:
            raise ValueError(f"{v2} not in graph")
        if e1 not in self:
            raise ValueError(f"{e1} not in graph")

        node = Node(x=e1.x, y=e1.y, h=1 - e1.B)

        self.remove_edge(v1, v2, e1)
        self.add_node(node)
        e1 = self.add_edge(v1, node)
        e2 = self.add_edge(node, v2)

        return node, e1, e2


    def visualize(self):
        pos = {node: (node.x, node.y) for node in self.G.nodes}
        labels = {}
        for node in self.G.nodes:
            if node.label == "V":
                labels[node] =  f"{node.label}\nh={node.h}"
            elif node.label == "S":
                labels[node] =  f"{node.label}\nR={node.R}"
            elif node.label == "E":
                labels[node] =  f"{node.label}\nB={node.B}"
        color_map = []

        for node in self.G:
            if node.label == "Q":
                color_map.append('lightgreen')
            elif node.label == "E":
                color_map.append("lightgrey")
            else:
                color_map.append('lightblue')

        nx.draw(self.G, pos=pos, with_labels=True, labels=labels, node_color=color_map, node_size=400, font_size=8,
                edge_color='gray')
        plt.show()

    # def visualize(self):
    #     pos = {node: (node.x, node.y) for node in self.G.nodes}
    #     labels = {node: node.label for node in self.G.nodes}
    #     color_map = []
    #
    #     for node in self.G:
    #         if node.label == "Q":
    #             color_map.append("lightgreen")
    #         elif node.label == "E":
    #             color_map.append("lightgrey")
    #         else:
    #             color_map.append("lightblue")
    #
    #     nx.draw(
    #         self.G,
    #         pos=pos,
    #         with_labels=True,
    #         labels=labels,
    #         node_color=color_map,
    #         node_size=400,
    #         font_size=10,
    #         edge_color="gray",
    #     )
    #     plt.show()
