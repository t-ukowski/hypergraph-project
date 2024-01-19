import unittest
from hypergraph.structures import Node, Graph
from hypergraph.productions.p6 import P6


class TestP6Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        self.prod = P6()

    def setUpLargerCompleteGraph(self):
        self.setUpCompleteGraph()
        node = Node(5, 2, 0)
        self.prod.nodes.append(node)
        self.prod.graph.add_node(node)
        self.prod.graph.add_edge(self.prod.nodes[4], node)

    def setUpIncompleteGraphWithMissingVertex(self):
        self.setUpCompleteGraph()
        self.prod.graph.remove_node(self.prod.nodes[3])

    def setUpIncompleteGraphWithMissingEdge(self):
        self.setUpCompleteGraph()
        self.prod.graph.remove_edge(
            self.prod.nodes[2], self.prod.nodes[4], self.prod.enodes[2]
        )

    def setUpGraphWithIncorrectR(self):
        self.setUpCompleteGraph()
        self.prod.qnode.R = 0

    def test_p6_production_applies(self):
        self.setUpCompleteGraph()
        # self.prod.graph.visualize()

        prod = P6()
        results = prod.search_for_subgraphs(self.prod.graph)

        for subgraph in results:
            prod.apply_production(self.prod.graph, subgraph)
            break

        # Aserty
        expected_num_nodes = 9
        self.assertEqual(self.prod.graph.get_number_of_nodes(), expected_num_nodes)

        expected_num_edges = 16
        self.assertEqual(self.prod.graph.get_number_of_edges(), expected_num_edges)
        # self.prod.graph.visualize()

    def test_p6_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        # self.prod.graph.visualize()

        prod = P6()
        results = prod.search_for_subgraphs(self.prod.graph)
        for subgraph in results:
            prod.apply_production(self.prod.graph, subgraph)
            break

        expected_num_nodes = 10
        self.assertEqual(self.prod.graph.get_number_of_nodes(), expected_num_nodes)

        expected_num_edges = 17
        self.assertEqual(self.prod.graph.get_number_of_edges(), expected_num_edges)
        # self.prod.graph.visualize()

    def test_p6_production_does_not_apply_because_missing_vertex(self):
        self.setUpIncompleteGraphWithMissingVertex()
        # self.prod.graph.visualize()

        prod = P6()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        self.assertEqual(len(results), 0)
        # self.prod.graph.visualize()

    def test_p6_production_does_not_apply_because_missing_edge(self):
        self.setUpIncompleteGraphWithMissingEdge()
        # self.prod.graph.visualize()

        prod = P6()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        self.assertEqual(len(results), 0)

    def test_p6_production_does_not_apply_because_incorrect_R(self):
        self.setUpGraphWithIncorrectR()
        # self.prod.graph.visualize()

        prod = P6()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        self.assertEqual(len(results), 0)
        # self.prod.graph.visualize()


if __name__ == "__main__":
    unittest.main()
