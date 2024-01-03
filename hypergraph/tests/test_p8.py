import unittest
from hypergraph.structures import Node, Graph
from hypergraph.productions.p8 import P8


class Testp8Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        self.prod = P8()

    def setUpLargerCompleteGraph(self):
        self.setUpCompleteGraph()
        node = Node(5, 2, 0)
        self.prod.nodes.append(node)
        self.prod.graph.add_node(node)
        self.prod.graph.add_edge(
            self.prod.nodes[4], node
        )

    def setUpIncompleteGraphWithMissingVertex(self):
        self.setUpCompleteGraph()
        self.prod.graph.remove_node(
            self.prod.nodes[3]
        )

    def setUpIncompleteGraphWithMissingEdge(self):
        self.setUpCompleteGraph()
        self.prod.graph.remove_edge(
            self.prod.nodes[2],
            self.prod.nodes[4],
            self.prod.enodes[1]
        )

    def setUpGraphWithIncorrectR(self):
        self.setUpCompleteGraph()
        self.prod.qnode.R = 1

    def test_p8_production_applies(self):
        self.setUpCompleteGraph()
        prod = P8()
        results = prod.search_for_subgraphs(self.prod.graph)

        for subgraph in results:
            prod.apply_production(self.prod.graph, subgraph)
            break

        # Aserty
        expected_num_nodes = 7
        self.assertEqual(self.prod.graph.get_number_of_nodes(), expected_num_nodes)

        expected_num_edges = 4
        self.assertEqual(self.prod.graph.get_number_of_edges(), expected_num_edges)

    def test_p8_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        prod = P8()
        results = prod.search_for_subgraphs(self.prod.graph)
        for subgraph in results:
            prod.apply_production(self.prod.graph, subgraph)
            break

        expected_num_nodes = 8
        self.assertEqual(self.prod.graph.get_number_of_nodes(), expected_num_nodes)

        expected_num_edges = 5
        self.assertEqual(self.prod.graph.get_number_of_edges(), expected_num_edges)

    def test_p8_production_does_not_apply_because_missing_vertex(self):
        self.setUpIncompleteGraphWithMissingVertex()
        prod = P8()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        self.assertEqual(len(results), 0)

    def test_p8_production_does_not_apply_because_missing_edge(self):
        self.setUpIncompleteGraphWithMissingEdge()
        prod = P8()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        self.assertEqual(len(results), 0)

    def test_p8_production_does_not_apply_because_incorrect_R(self):
        self.setUpGraphWithIncorrectR()
        prod = P8()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()