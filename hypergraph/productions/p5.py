from hypergraph.productions.production_base import ProductionBase
from hypergraph.structures import Graph, Node, QNode, ENode
import networkx as nx


class P5(ProductionBase):
    def __init__(self):
        super().__init__()
        node1 = Node(0, 0, 0)
        node2 = Node(10, 0, 0)
        node3 = Node(10, 10, 0)
        node4 = Node(0, 10, 0)
        node5 = Node(10, 5, 1)
        node6 = Node(5, 0, 1)
        node7 = Node(0, 5, 1)

        self.nodes = [node1, node2, node3, node4, node5, node6, node7]
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)
        self.graph.add_node(node5)
        self.graph.add_node(node6)
        self.graph.add_node(node7)
        self.qnode = self.graph.add_q_node(node1, node2, node3, node4)
        self.qnode.R = 1
        enode1 = self.graph.add_edge(node1, node6)
        enode2 = self.graph.add_edge(node2, node5)
        enode3 = self.graph.add_edge(node5, node3)
        enode4 = self.graph.add_edge(node3, node4)
        enode5 = self.graph.add_edge(node4, node7)
        enode6 = self.graph.add_edge(node7, node1)
        enode7 = self.graph.add_edge(node6, node2)

        self.enodes = [enode1, enode2, enode3, enode4, enode5, enode6, enode7]
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
        if n1.label == "V":
            if n1.h != n2.h:
                return False
        return True

    def apply_production(self, graph, mapping):
        mapping = {v: k for k, v in mapping.items()}
        # Split 4 edges
        # v1, v1_e1, v1_e2 = graph.split_edge(mapping[self.nodes[0]], mapping[self.nodes[1]], mapping[self.enodes[0]])
        v3, v3_e1, v3_e2 = graph.split_edge(
            mapping[self.nodes[2]], mapping[self.nodes[3]], mapping[self.enodes[3]]
        )
        # Replace midpoint
        node = Node(x=mapping[self.qnode].x, y=mapping[self.qnode].y, h=0)
        graph.remove_q_node(mapping[self.qnode])
        graph.add_node(node)

        mapping[self.nodes[6]].h = 0
        mapping[self.nodes[5]].h = 0
        mapping[self.nodes[4]].h = 0

        enode = mapping[self.enodes[3]]
        v3.h = 1 - enode.B

        # Add inside edges
        graph.add_edge(mapping[self.nodes[4]], node)
        graph.add_edge(v3, node)
        graph.add_edge(mapping[self.nodes[6]], node)
        graph.add_edge(mapping[self.nodes[5]], node)

        # Add hyperedges
        graph.add_q_node(mapping[self.nodes[3]], v3, node, mapping[self.nodes[6]])
        graph.add_q_node(v3, node, mapping[self.nodes[4]], mapping[self.nodes[2]])
        graph.add_q_node(
            mapping[self.nodes[6]], mapping[self.nodes[0]], mapping[self.nodes[5]], node
        )
        graph.add_q_node(
            node, mapping[self.nodes[5]], mapping[self.nodes[1]], mapping[self.nodes[4]]
        )
