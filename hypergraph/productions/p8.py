from hypergraph.productions.production_base import ProductionBase
from hypergraph.structures import  Graph, Node, QNode, ENode
import networkx as nx

class P8(ProductionBase):
    def __init__(self):
        super().__init__()
        node1 = Node(0, 0, 0)
        node2 = Node(10, 0, 0)
        node3 = Node(10, 10, 0)
        node4 = Node(0, 10, 0)
        node5 = Node(10, 5, 1)
        node6 = Node(20, 5, 0)
        node7 = Node(20, 10, 0)
        
        self.nodes = [node1, node2, node3, node4, node5, node6, node7]
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)
        self.graph.add_node(node5)
        self.graph.add_node(node6)
        self.graph.add_node(node7)
        
        self.qnode = self.graph.add_q_node(node1, node2, node3, node4)
        self.qnode.R = 0
        self.qnode2 = self.graph.add_q_node(node3, node5, node6, node7)
        self.qnode2.R = 1
        
        
        enode1 = self.graph.add_edge(node2, node5)
        enode2 = self.graph.add_edge(node5, node3)
        self.enodes = [enode1, enode2]
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
        if n1.label == "V":
            if n1.h != n2.h:
                return False
        return True

    def apply_production(self, graph, mapping):
        mapping = {v: k for k, v in mapping.items()}
        mapping[self.qnode].R = 1