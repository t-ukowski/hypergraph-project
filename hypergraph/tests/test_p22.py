import unittest
from hypergraph.structures import Node
from hypergraph.productions.p22 import P22


class TestP22Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p7_production_applies)
        self.prod = P22()

    def setUpLargerCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p1_production_applies_to_larger_graph)
        self.setUpCompleteGraph()
        node = Node(5, 2, 0)
        self.prod.nodes.append(node)
        self.prod.graph.add_node(node)  # Dodanie nowego węzła
        self.prod.graph.add_edge(
            self.prod.nodes[4], node
        )  # Dodanie krawędzi między nowym węzłem a węzłem 4

    def setUpIncompleteGraphWithMissingVertex(self):
        # Ustawienie dla niekompletnego grafu (używane w teście test_p1_production_does_not_apply_because_missing_vertex)
        self.setUpCompleteGraph()
        self.prod.graph.remove_node(
            self.prod.nodes[3]
        )  # Celowo pomijamy czwarty węzeł i jego krawędzie

    def setUpGraphWithIncorrectR(self):
        self.setUpCompleteGraph()
        self.prod.snode.R = 1  # Ustawienie R na niepoprawną wartość

    def test_p22_production_applies(self):
        self.setUpCompleteGraph()

        prod = P22()
        results = prod.search_for_subgraphs(self.prod.graph)

        for subgraph in results:
            self.prod.apply_production(self.prod.graph, subgraph)
            break

        self.assertEqual(self.prod.snode.R, 1)

    def test_p22_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        self.prod.graph.visualize()

        prod = P22()
        results = prod.search_for_subgraphs(prod.graph)
        for subgraph in results:
            self.prod.apply_production(self.prod.graph, subgraph)
            break
        self.prod.graph.visualize()

        self.assertEqual(self.prod.snode.R,  1)


    def test_p22_production_doesnt_apply_to_incomplete_graph(self):
        self.setUpIncompleteGraphWithMissingVertex()
        prod = P22()
        results = prod.search_for_subgraphs(self.prod.graph)
        for subgraph in results:
            self.prod.apply_production(self.prod.graph, subgraph)
            break

        self.assertEqual(self.prod.snode.R, 0)

    def test_p22_production_doesnt_apply_to_incorrect_graph(self):
        self.setUpGraphWithIncorrectR()
        prod = P22()
        results = prod.search_for_subgraphs(self.prod.graph)

        self.assertEqual(len(list(results)), 0)


if __name__ == '__main__':
    unittest.main()