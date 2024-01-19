from hypergraph.productions.production_base import ProductionBase
from hypergraph.structures import Graph, Node
from typing import *


class P11(ProductionBase):
    def __init__(self):
        super().__init__()
        self.nodes = [
            Node(0, 0, 0),
            Node(2, 0, 0),
            Node(2, 4, 0),
            Node(0, 4, 0),
            Node(4, 2, 0),
            Node(-2, 2, 0),
            Node(1, 0, 1),
            Node(-1, 1, 1),
        ]

        self.nodes_in_order = [
            self.nodes[0],
            self.nodes[6],
            self.nodes[1],
            self.nodes[4],
            self.nodes[2],
            self.nodes[3],
            self.nodes[5],
            self.nodes[7],
        ]

        for node in self.nodes:
            self.graph.add_node(node)

        self.qnode = self.graph.add_s_node(
            self.nodes[0],
            self.nodes[1],
            self.nodes[2],
            self.nodes[3],
            self.nodes[4],
            self.nodes[5],
        )

        self.qnode.R = 1

        self.enodes_dict = {
            (n1, n2): self.graph.add_edge(n1, n2)
            for n1, n2 in zip(
                self.nodes_in_order, self.nodes_in_order[1:] + [self.nodes_in_order[0]]
            )
        }

        self.enodes = list(self.enodes_dict.values())

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

    def apply_production(self, graph: Graph, mapping: Dict):
        mapping = {v: k for k, v in mapping.items()}

        # Split 4 edges
        v_2_5, _, _ = graph.split_edge(
            mapping[self.nodes[1]],
            mapping[self.nodes[4]],
            mapping[self.enodes_dict[(self.nodes[1], self.nodes[4])]],
        )

        v_5_3, _, _ = graph.split_edge(
            mapping[self.nodes[4]],
            mapping[self.nodes[2]],
            mapping[self.enodes_dict[(self.nodes[4], self.nodes[2])]],
        )

        v_3_4, _, _ = graph.split_edge(
            mapping[self.nodes[2]],
            mapping[self.nodes[3]],
            mapping[self.enodes_dict[(self.nodes[2], self.nodes[3])]],
        )

        v_4_6, _, _ = graph.split_edge(
            mapping[self.nodes[3]],
            mapping[self.nodes[5]],
            mapping[self.enodes_dict[(self.nodes[3], self.nodes[5])]],
        )

        nodes_in_order = [
            mapping[self.nodes[0]],
            mapping[self.nodes[6]],
            mapping[self.nodes[1]],
            v_2_5,
            mapping[self.nodes[4]],
            v_5_3,
            mapping[self.nodes[2]],
            v_3_4,
            mapping[self.nodes[3]],
            v_4_6,
            mapping[self.nodes[5]],
            mapping[self.nodes[7]],
        ]

        mapping[self.nodes[6]].h = 0
        mapping[self.nodes[7]].h = 0

        mid_node = Node(x=mapping[self.qnode].x, y=mapping[self.qnode].y, h=0)

        graph.remove_q_node(mapping[self.qnode])
        graph.add_node(mid_node)

        # Add inside edges
        add_inside_edges(graph, nodes_in_order, mid_node)

        # Add hyperedges
        add_q_nodes(graph, nodes_in_order, mid_node)



def add_q_nodes(graph: Graph, nodes_in_order: List[Node], mid_node: Node):
    n = len(nodes_in_order)
    for i in range(-1, n - 1, 2):
        graph.add_q_node(
            nodes_in_order[i % n],
            nodes_in_order[(i + 1) % n],
            nodes_in_order[(i + 2) % n],
            mid_node,
        )


def add_inside_edges(graph: Graph, nodes_in_order: List[Node], mid_node: Node):
    n = len(nodes_in_order)
    for i in range(1, n, 2):
        graph.add_edge(
            nodes_in_order[i],
            mid_node,
        )
