from hypergraph.productions.production_base import ProductionBase
from hypergraph.structures import Graph, Node, QNode, ENode
import networkx as nx


class P1(ProductionBase):
    def __init__(self):
        super().__init__()
        node1 = Node(0, 0, 0)
        node2 = Node(2, 0, 0)
        node3 = Node(2, 2, 0)
        node4 = Node(0, 2, 0)
        self.nodes = [node1, node2, node3, node4]
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)
        self.qnode = self.graph.add_q_node(node1, node2, node3, node4)
        self.qnode.R = 1
        enode1 = self.graph.add_edge(node1, node2)
        enode2 = self.graph.add_edge(node2, node3)
        enode3 = self.graph.add_edge(node3, node4)
        enode4 = self.graph.add_edge(node4, node1)
        self.enodes = [enode1, enode2, enode3, enode4]
        self.left_graph = self.graph

    # Predykat stosowalnosci
    def node_match(self, n1, n2):
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
        # Split 4 edges
        v1, v1_e1, v1_e2 = graph.split_edge(
            mapping[self.nodes[0]], mapping[self.nodes[1]], mapping[self.enodes[0]]
        )
        v2, v2_e1, v2_e2 = graph.split_edge(
            mapping[self.nodes[1]], mapping[self.nodes[2]], mapping[self.enodes[1]]
        )
        v3, v3_e1, v3_e2 = graph.split_edge(
            mapping[self.nodes[2]], mapping[self.nodes[3]], mapping[self.enodes[2]]
        )
        v4, v4_e1, v4_e2 = graph.split_edge(
            mapping[self.nodes[3]], mapping[self.nodes[0]], mapping[self.enodes[3]]
        )
        # Replace midpoint
        node = Node(x=mapping[self.qnode].x, y=mapping[self.qnode].y, h=0)
        graph.remove_q_node(mapping[self.qnode])
        graph.add_node(node)
        # Add inside edges
        graph.add_edge(v1, node)
        graph.add_edge(v2, node)
        graph.add_edge(v3, node)
        graph.add_edge(v4, node)
        # Add hyperedges
        graph.add_q_node(mapping[self.nodes[0]], v1, node, v4)
        graph.add_q_node(mapping[self.nodes[1]], v1, node, v2)
        graph.add_q_node(node, v2, mapping[self.nodes[2]], v3)
        graph.add_q_node(v4, node, v3, mapping[self.nodes[3]])
