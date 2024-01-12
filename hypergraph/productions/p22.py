from hypergraph.productions.production_base import ProductionBase
from hypergraph.structures import  Graph, Node, QNode, ENode
import networkx as nx

class P22(ProductionBase):
    def __init__(self):
        super().__init__()
        self.nodes = [
            Node(0, 0, 0),  # 1
            Node(2, 0, 0),  # 2
            Node(2, 2, 0),  # 3
            Node(0, 2, 0),  # 4
            Node(2, 1, 0),  # 5
            Node(4, 1, 0),  # 6
            Node(4, 2, 0),  # 7
            Node(1, 0, 0),  # 8
            Node(0, 1, 0)   # 9

        ]

        for node in self.nodes:
            self.graph.add_node(node)

        self.snode = self.graph.add_s_node(
            self.nodes[0],
            self.nodes[1],
            self.nodes[2],
            self.nodes[3],
            self.nodes[7],
            self.nodes[8],
        )

        self.snode.R = 0

        self.qnode = self.graph.add_q_node(
            self.nodes[2],
            self.nodes[4],
            self.nodes[5],
            self.nodes[6]
        )

        self.qnode.R = 1

        self.graph.add_edge(self.nodes[1], self.nodes[4])
        self.graph.add_edge(self.nodes[4], self.nodes[2])

        self.left_graph = self.graph

    # Predykat stosowalnosci
    def node_match(self, n1: Node, n2: Node):
        n1 = n1["node"]
        n2 = n2["node"]
        if n1.label != n2.label:
            return False
        if n1.label == "Q":
            if n1.R != n2.R:
                return False
        if n1.label == "S":
            if n1.R != n2.R:
                return False
        if n1.label == "V":
            if n1.h != n2.h:
                return False
        return True

    def apply_production(self, graph, mapping):
        mapping = {v: k for k, v in mapping.items()}
        mapping[self.snode].R = 1
        print(mapping[self.snode].R)
