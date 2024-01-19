from hypergraph.productions.production_base import ProductionBase
from hypergraph.structures import  Graph, Node, QNode, ENode
import networkx as nx

class P7(ProductionBase):
    def __init__(self):
        super().__init__()
        node1 = Node(0, 0, 0)
        node2 = Node(10, 0, 0)
        node3 = Node(10, 10, 0)
        node4 = Node(0, 10, 0)
        self.nodes = [node1, node2, node3, node4]
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)
        self.qnode = self.graph.add_q_node(node1, node2, node3, node4)
        self.qnode.R = 0
        self.left_graph = self.graph

    # Predykat stosowalnosci
    def node_match(self, n1, n2):
        n1 = n1['node']
        n2 = n2['node']
        if n1.label != n2.label:
            return False
        if n1.label == "Q":
            if n1.R != n2.R:
                return False
        return True

    def apply_production(self, graph, mapping):
        mapping = {v: k for k, v in mapping.items()}
        graph.remove_q_node(mapping[self.qnode])
        graph.add_q_node(mapping[self.nodes[0]], mapping[self.nodes[1]], mapping[self.nodes[2]], mapping[self.nodes[3]], 1)

