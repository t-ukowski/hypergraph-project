import unittest
from hypergraph.structures import Node
from hypergraph.productions.p10 import P10


class TestP9Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p10_production_applies)
        self.prod = P10()

    def setUpLargerCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p10_production_applies_to_larger_graph)
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
            self.prod.nodes[1],
            self.prod.nodes[4],
            self.prod.enodes[2],
        )  # Celowo pomijamy krawędź między node1 a node2
        # Celowo pomijamy krawędź między node3 a node4

    def setUpGraphWithIncorrectR(self):
        # Ustawienie dla grafu z niepoprawną wartością R (używane w teście test_p1_production_does_not_apply_because_incorrect_R)
        self.setUpCompleteGraph()
        self.prod.snode.R = 0  # Ustawienie R na niepoprawną wartość

    def test_p10_production_applies(self):
        self.setUpCompleteGraph()
        prod = P10()
        results = prod.search_for_subgraphs(self.prod.graph)

        for subgraph in results:
            prod.apply_production(self.prod.graph, subgraph)
            break

        expected_num_nodes = 13  # Dodano jeden nowy węzeł w centrum i  4 na bokach
        self.assertEqual(self.prod.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 24
        self.assertEqual(self.prod.graph.get_number_of_edges(), expected_num_edges)

    def test_p10_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        self.prod.graph.visualize()
        results = self.prod.search_for_subgraphs(self.prod.graph)
        for subgraph in results:
            self.prod.apply_production(self.prod.graph, subgraph)
            break

        self.prod.graph.visualize()
        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 14  # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.prod.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 25  # 4 oryginalne krawędzie są podzielone na 8, a do węzła centralnego dodane są 4 nowe krawędzie
        self.assertEqual(self.prod.graph.get_number_of_edges(), expected_num_edges)

    def test_p10_production_does_not_apply_because_missing_vertex(self):
        self.setUpIncompleteGraphWithMissingVertex()  # Ustawienie niekompletnego grafu dla tego testu
        self.prod.graph.visualize()
        prod = P10()
        results = list(prod.search_for_subgraphs(self.prod.graph))
        self.prod.graph.visualize()

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana)
        self.assertEqual(len(results), 0)

    def test_p10_production_does_not_apply_because_missing_edge(self):
        self.setUpIncompleteGraphWithMissingEdge()  # Ustawienie grafu z brakującą krawędzią dla tego testu
        prod = P10()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z brakującą krawędzią)
        self.assertEqual(len(results), 0)

    def test_p10_production_does_not_apply_because_incorrect_R(self):
        self.setUpGraphWithIncorrectR()  # Ustawienie grafu z niepoprawną wartością R dla tego testu
        prod = P10()
        results = list(prod.search_for_subgraphs(self.prod.graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z niepoprawną wartością R)
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
