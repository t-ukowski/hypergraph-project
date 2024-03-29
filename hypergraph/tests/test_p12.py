import unittest
from hypergraph.structures import Node
from hypergraph.productions.p12 import P12
from hypergraph.productions.p13 import P13


class TestP12Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p13_production_applies)
        self.prop = P12()

    def setUpLargerCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p1_production_applies_to_larger_graph)
        self.setUpCompleteGraph()
        node = Node(5, 2, 0)
        self.prop.nodes.append(node)
        self.prop.graph.add_node(node)  # Dodanie nowego węzła
        self.prop.graph.add_edge(
            self.prop.nodes[4], node
        )  # Dodanie krawędzi między nowym węzłem a węzłem 4

    def setUpIncompleteGraphWithMissingVertex(self):
        # Ustawienie dla niekompletnego grafu (używane w teście test_p1_production_does_not_apply_because_missing_vertex)
        self.setUpCompleteGraph()
        self.prop.graph.remove_node(
            self.prop.nodes[3]
        )  # Celowo pomijamy czwarty węzeł i jego krawędzie
        # Celowo pomijamy czwarty węzeł i jego krawędzie

    def setUpIncompleteGraphWithMissingEdge(self):
        # Ustawienie dla grafu z brakującą krawędzią (używane w teście test_p1_production_does_not_apply_because_missing_edge)
        self.setUpCompleteGraph()
        self.prop.graph.remove_edge(
            self.prop.nodes_in_order[0],
            self.prop.nodes_in_order[1],
            self.prop.enodes_dict[
                (self.prop.nodes_in_order[0], self.prop.nodes_in_order[1])
            ],
        )  # Celowo pomijamy krawędź między node1 a node2
        # Celowo pomijamy krawędź między node3 a node4

    def setUpGraphWithIncorrectR(self):
        # Ustawienie dla grafu z niepoprawną wartością R (używane w teście test_p1_production_does_not_apply_because_incorrect_R)
        self.setUpCompleteGraph()
        self.prop.qnode.R = 0  # Ustawienie R na niepoprawną wartość

    def setUpDifferentGraph(self):
        # Ustawienie grafu o innej pozycji hanging node (tutaj takiej jak w lewej stronie P13)
        self.prop = P13()

    def test_p12_production_applies(self):
        self.setUpCompleteGraph()
        prod = P12()
        results = prod.search_for_subgraphs(self.prop.graph)

        for subgraph in results:
            prod.apply_production(self.prop.graph, subgraph)
            break

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 13  # Dodano jeden nowy węzeł w centrum i  4 na bokach
        self.assertEqual(self.prop.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 24
        self.assertEqual(self.prop.graph.get_number_of_edges(), expected_num_edges)
        # Hanging node
        self.assertEqual(self.prop.nodes[6].h, 0)
        self.assertEqual(self.prop.nodes[7].h, 0)

    def test_p12_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        prod = P12()

        results = prod.search_for_subgraphs(self.prop.graph)
        for subgraph in results:
            prod.apply_production(self.prop.graph, subgraph)
            break

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 14  # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.prop.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 25  # 4 oryginalne krawędzie są podzielone na 8, a do węzła centralnego dodane są 4 nowe krawędzie
        self.assertEqual(self.prop.graph.get_number_of_edges(), expected_num_edges)
        # Hanging node
        self.assertEqual(self.prop.nodes[6].h, 0)
        self.assertEqual(self.prop.nodes[7].h, 0)

    def test_p12_production_applies_to_larger_graph_with_border_edge(self):
        self.setUpLargerCompleteGraph()
        prod = P12()
        self.prop.enodes_dict[self.prop.nodes[2], self.prop.nodes[3]].B = 1

        results = prod.search_for_subgraphs(self.prop.graph)
        for subgraph in results:
            prod.apply_production(self.prop.graph, subgraph)
            break

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 14  # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.prop.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 25  # 4 oryginalne krawędzie są podzielone na 8, a do węzła centralnego dodane są 4 nowe krawędzie
        self.assertEqual(self.prop.graph.get_number_of_edges(), expected_num_edges)
        # Hanging node
        self.assertEqual(self.prop.nodes[6].h, 0)
        self.assertEqual(self.prop.nodes[7].h, 0)

    def test_p12_production_does_not_apply_because_missing_vertex(self):
        self.setUpIncompleteGraphWithMissingVertex()  # Ustawienie niekompletnego grafu dla tego testu
        prod = P12()

        results = list(prod.search_for_subgraphs(self.prop.graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana)
        self.assertEqual(len(results), 0)

    def test_p12_production_does_not_apply_because_missing_edge(self):
        self.setUpIncompleteGraphWithMissingEdge()  # Ustawienie grafu z brakującą krawędzią dla tego testu
        prod = P12()

        results = list(prod.search_for_subgraphs(self.prop.graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z brakującą krawędzią)
        self.assertEqual(len(results), 0)

    def test_p12_production_does_not_apply_because_incorrect_R(self):
        self.setUpGraphWithIncorrectR()  # Ustawienie grafu z niepoprawną wartością R dla tego testu
        prod = P12()

        results = list(prod.search_for_subgraphs(self.prop.graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z niepoprawną wartością R)
        self.assertEqual(len(results), 0)

    def test_p12_production_does_not_apply_because_of_different_graph(self):
        self.setUpDifferentGraph()  # Ustawienie lewej strony na inną niż oczekiwana przez P12
        prod = P12()

        results = list(prod.search_for_subgraphs(self.prop.graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z niepoprawną wartością R)
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
