from typing import Dict

from hypergraph.productions.production_base import ProductionBase
from hypergraph.structures import Node, Graph


class P9(ProductionBase):
    def __init__(self):
        super().__init__()
        self.nodes = [
            Node(0, 0, 0),  # 1
            Node(2, 0, 0),  # 2
            Node(2, 2, 0),  # 3
            Node(0, 2, 0),  # 4
            Node(3, 1, 0),  # 5
            Node(-1, 1, 0),  # 6
        ]

        for node in self.nodes:
            self.graph.add_node(node)

        self.snode = self.graph.add_s_node(
            self.nodes[0],
            self.nodes[1],
            self.nodes[2],
            self.nodes[3],
            self.nodes[4],
            self.nodes[5],
        )

        self.snode.R = 1

        self.enode1 = self.graph.add_edge(self.nodes[0], self.nodes[1])
        self.enode2 = self.graph.add_edge(self.nodes[1], self.nodes[4])
        self.enode3 = self.graph.add_edge(self.nodes[4], self.nodes[2])
        self.enode4 = self.graph.add_edge(self.nodes[2], self.nodes[3])
        self.enode5 = self.graph.add_edge(self.nodes[3], self.nodes[5])
        self.enode6 = self.graph.add_edge(self.nodes[5], self.nodes[0])
        self.enodes = [
            self.enode1,
            self.enode2,
            self.enode3,
            self.enode4,
            self.enode5,
            self.enode6,
        ]

        self.left_graph = self.graph

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

        # Split edges
        v_1_2, _, _ = graph.split_edge(
            mapping[self.nodes[0]],
            mapping[self.nodes[1]],
            mapping[self.enodes[0]],
        )
        v_2_5, _, _ = graph.split_edge(
            mapping[self.nodes[1]],
            mapping[self.nodes[4]],
            mapping[self.enodes[1]],
        )

        v_5_3, _, _ = graph.split_edge(
            mapping[self.nodes[4]],
            mapping[self.nodes[2]],
            mapping[self.enodes[2]],
        )

        v_3_4, _, _ = graph.split_edge(
            mapping[self.nodes[2]],
            mapping[self.nodes[3]],
            mapping[self.enodes[3]],
        )

        v_4_6, _, _ = graph.split_edge(
            mapping[self.nodes[3]],
            mapping[self.nodes[5]],
            mapping[self.enodes[4]],
        )

        v_6_1, _, _ = graph.split_edge(
            mapping[self.nodes[5]],
            mapping[self.nodes[0]],
            mapping[self.enodes[5]],
        )

        v_nodes_array = [v_1_2, v_2_5, v_5_3, v_3_4, v_4_6, v_6_1]

        mid_node = Node(x=mapping[self.snode].x, y=mapping[self.snode].y, h=0)

        graph.remove_q_node(mapping[self.snode])

        graph.add_node(mid_node)

        # add enodes
        for node in v_nodes_array:
            graph.add_edge(node, mid_node)

        # add qnodes
        graph.add_q_node(
            mapping[self.nodes[0]],
            v_1_2,
            mid_node,
            v_6_1,
        )

        graph.add_q_node(
            mapping[self.nodes[1]],
            v_1_2,
            mid_node,
            v_2_5,
        )
        graph.add_q_node(
            mapping[self.nodes[4]],
            v_2_5,
            mid_node,
            v_5_3,
        )
        graph.add_q_node(
            mapping[self.nodes[2]],
            v_5_3,
            mid_node,
            v_3_4,
        )
        graph.add_q_node(
            mapping[self.nodes[3]],
            v_3_4,
            mid_node,
            v_4_6,
        )
        graph.add_q_node(
            mapping[self.nodes[5]],
            v_4_6,
            mid_node,
            v_6_1,
        )
