import unittest
from hypergraph.structures import Node, Graph
from hypergraph.productions.p21 import P21


class TestP21Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p7_production_applies)
        self.prod = P21()

    def setUpLargerCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p7_production_applies_to_larger_graph)
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

    def setUpIncompleteGraphWithMissingEdge(self):
        # Ustawienie dla grafu z brakującą krawędzią (używane w teście test_p1_production_does_not_apply_because_missing_edge)
        self.setUpCompleteGraph()
        self.prod.graph.remove_edge(
            self.prod.nodes[0],
            self.prod.nodes[4],
        )  # Celowo pomijamy krawędź między node1 a node2
        # Celowo pomijamy krawędź między node3 a node4


    def setUpGraphWithIncorrectR(self):
        self.setUpCompleteGraph()
        self.prod.snode.R = 1  # Ustawienie R na niepoprawną wartość

    def test_p21_production_applies(self):
        self.setUpCompleteGraph()

        results = self.prod.search_for_subgraphs(self.prod.graph)

        for subgraph in results:
            self.prod.apply_production(self.prod.graph, subgraph)
            break

        self.assertEqual(self.prod.snode.R, 1)


    def test_p21_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        self.prod.graph.visualize()

        results = self.prod.search_for_subgraphs(self.prod.graph)
        for subgraph in results:
            self.prod.apply_production(self.prod.graph, subgraph)
            break
        self.prod.graph.visualize()

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 7  # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.prod.snode.R,  1)

    def test_p21_production_does_not_apply_because_missing_vertex(self):
        self.setUpIncompleteGraphWithMissingVertex()  # Ustawienie niekompletnego grafu dla tego testu
        self.prod.graph.visualize()
        prod = P21()
        results = list(prod.search_for_subgraphs(self.prod.graph))
        self.prod.graph.visualize()

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana)
        self.assertEqual(len(results), 0)

    def test_p21_production_does_not_apply_because_incorrect_R(self):
        self.setUpGraphWithIncorrectR()  # Ustawienie grafu z niepoprawną wartością R dla tego testu
        self.prod.graph.visualize()
        prod = P21()
        results = list(prod.search_for_subgraphs(self.prod.graph))
        self.prod.graph.visualize()

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z niepoprawną wartością R)
        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()