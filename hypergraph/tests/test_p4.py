import unittest
from hypergraph.structures import Node, Graph
from hypergraph.productions.p4 import P4


class TestP4Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p4_production_applies)
        self.node1 = Node(0, 0, 0)
        self.node2 = Node(5, 0, 0)
        self.node3 = Node(5, 5, 0)
        self.node4 = Node(0, 5, 0)
        self.node5 = Node(5, 2.5, 1)
        self.node6 = Node(0, 2.5, 1)
        self.graph = Graph()
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_node(self.node3)
        self.graph.add_node(self.node4)
        self.graph.add_node(self.node5)
        self.graph.add_node(self.node6)
        self.qnode = self.graph.add_q_node(self.node1, self.node2, self.node3, self.node4)
        self.qnode.R = 1
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node2, self.node5)
        self.graph.add_edge(self.node5, self.node3)
        self.graph.add_edge(self.node3, self.node4)
        self.graph.add_edge(self.node4, self.node6)
        self.graph.add_edge(self.node6, self.node1)

    def setUpRolledGraph(self):
        # Ustawienie dla kompletnego grafu obroconego(używane w teście test_p4_production_applies_to_rolled_graph)
        self.node1 = Node(0, 0, 0)
        self.node2 = Node(5, 0, 0)
        self.node3 = Node(5, 5, 0)
        self.node4 = Node(0, 5, 0)
        self.node5 = Node(2.5, 0, 1)
        self.node6 = Node(2.5, 5, 1)
        self.graph = Graph()
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_node(self.node3)
        self.graph.add_node(self.node4)
        self.graph.add_node(self.node5)
        self.graph.add_node(self.node6)
        self.qnode = self.graph.add_q_node(self.node1, self.node2, self.node3, self.node4)
        self.qnode.R = 1
        self.graph.add_edge(self.node1, self.node5)
        self.graph.add_edge(self.node5, self.node2)
        self.graph.add_edge(self.node2, self.node3)
        self.graph.add_edge(self.node3, self.node6)
        self.graph.add_edge(self.node6, self.node4)
        self.graph.add_edge(self.node4, self.node1)

    def setUpLargerCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p4_production_applies_to_larger_graph)
        self.node1 = Node(0, 0, 0)
        self.node2 = Node(5, 0, 0)
        self.node3 = Node(5, 5, 0)
        self.node4 = Node(0, 5, 0)
        self.node5 = Node(5, 2.5, 1)
        self.node6 = Node(0, 2.5, 1)
        self.node7 = Node(5, 10, 0)
        self.node8 = Node(0, 10, 0)
        self.graph = Graph()
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_node(self.node3)
        self.graph.add_node(self.node4)
        self.graph.add_node(self.node5)
        self.graph.add_node(self.node6)
        self.graph.add_node(self.node7)
        self.graph.add_node(self.node8)
        self.qnode = self.graph.add_q_node(self.node1, self.node2, self.node3, self.node4)
        self.qnode.R = 1
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node2, self.node5)
        self.graph.add_edge(self.node5, self.node3)
        self.graph.add_edge(self.node3, self.node4)
        self.graph.add_edge(self.node4, self.node6)
        self.graph.add_edge(self.node6, self.node1)
        self.graph.add_edge(self.node4, self.node7)
        self.graph.add_edge(self.node4, self.node8)

    def setUpIncompleteGraphWithMissingVertex(self):
        # Ustawienie dla niekompletnego grafu (używane w teście test_p4_production_does_not_apply_because_missing_vertex)
        self.incomplete_node1 = Node(0, 0, 0)
        self.incomplete_node2 = Node(2, 0, 0)
        self.incomplete_node3 = Node(2, 2, 0)
        self.incomplete_node4 = Node(1, 0, 0)
        self.incomplete_graph = Graph()
        self.incomplete_graph.add_node(self.incomplete_node1)
        self.incomplete_graph.add_node(self.incomplete_node2)
        self.incomplete_graph.add_node(self.incomplete_node3)
        self.incomplete_graph.add_node(self.incomplete_node4)
        self.incomplete_graph.add_edge(self.incomplete_node1, self.incomplete_node4)
        self.incomplete_graph.add_edge(self.incomplete_node4, self.incomplete_node2)
        self.incomplete_graph.add_edge(self.incomplete_node2, self.incomplete_node3)
        # Celowo pomijamy czwarty węzeł i jego krawędzie

    def setUpIncompleteGraphWithMissingEdge(self):
        # Ustawienie dla grafu z brakującą krawędzią (używane w teście test_p4_production_does_not_apply_because_missing_edge)
        self.missing_edge_node1 = Node(0, 0, 0)
        self.missing_edge_node2 = Node(5, 0, 0)
        self.missing_edge_node3 = Node(5, 5, 0)
        self.missing_edge_node4 = Node(0, 5, 0)
        self.missing_edge_node5 = Node(2.5, 0, 1)
        self.missing_edge_node6 = Node(2.5, 5, 1)
        self.missing_edge_graph = Graph()
        self.missing_edge_graph.add_node(self.missing_edge_node1)
        self.missing_edge_graph.add_node(self.missing_edge_node2)
        self.missing_edge_graph.add_node(self.missing_edge_node3)
        self.missing_edge_graph.add_node(self.missing_edge_node4)
        self.missing_edge_graph.add_node(self.missing_edge_node5)
        self.missing_edge_graph.add_node(self.missing_edge_node6)
        self.missing_edge_qnode = self.missing_edge_graph.add_q_node(self.missing_edge_node1, self.missing_edge_node2,
                                                                     self.missing_edge_node3, self.missing_edge_node4)
        self.missing_edge_qnode.R = 1
        self.missing_edge_graph.add_edge(self.missing_edge_node1, self.missing_edge_node5)
        self.missing_edge_graph.add_edge(self.missing_edge_node5, self.missing_edge_node2)
        self.missing_edge_graph.add_edge(self.missing_edge_node2, self.missing_edge_node3)
        self.missing_edge_graph.add_edge(self.missing_edge_node3, self.missing_edge_node6)
        self.missing_edge_graph.add_edge(self.missing_edge_node6, self.missing_edge_node4)

    def setUpGraphWithIncorrectR(self):
        # Ustawienie dla grafu z niepoprawną wartością R (używane w teście test_p4_production_does_not_apply_because_incorrect_R)
        self.incorrect_r_node1 = Node(0, 0, 0)
        self.incorrect_r_node2 = Node(5, 0, 0)
        self.incorrect_r_node3 = Node(5, 5, 0)
        self.incorrect_r_node4 = Node(0, 5, 0)
        self.incorrect_r_node5 = Node(5, 2.5, 1)
        self.incorrect_r_node6 = Node(0, 2.5, 1)
        self.incorrect_r_graph = Graph()
        self.incorrect_r_graph.add_node(self.incorrect_r_node1)
        self.incorrect_r_graph.add_node(self.incorrect_r_node2)
        self.incorrect_r_graph.add_node(self.incorrect_r_node3)
        self.incorrect_r_graph.add_node(self.incorrect_r_node4)
        self.incorrect_r_graph.add_node(self.incorrect_r_node5)
        self.incorrect_r_graph.add_node(self.incorrect_r_node6)
        self.incorrect_r_qnode = self.incorrect_r_graph.add_q_node(self.incorrect_r_node1, self.incorrect_r_node2,
                                                                   self.incorrect_r_node3, self.incorrect_r_node4)
        self.incorrect_r_qnode.R = 0  # ustawienie R na niepoprawną wartość
        self.incorrect_r_graph.add_edge(self.incorrect_r_node1, self.incorrect_r_node2)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node2, self.incorrect_r_node5)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node5, self.incorrect_r_node3)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node3, self.incorrect_r_node4)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node4, self.incorrect_r_node6)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node6, self.incorrect_r_node1)

    def test_p4_production_applies(self):
        self.setUpCompleteGraph()
        # self.graph.visualize()
        prod = P4()
        results = prod.search_for_subgraphs(self.graph)
        for subgraph in results:
            prod.apply_production(self.graph, subgraph)
            break

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 9  # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 16  # 4 oryginalne krawędzie są podzielone na 8, a do węzła centralnego dodane są 4 nowe krawędzie
        self.assertEqual(self.graph.get_number_of_edges(), expected_num_edges)

        # 3. Sprawdź obecność nowego centralnego węzła i jego właściwości
        central_node = None
        for node in self.graph.get_nodes():
            if node.label == "V" and node.h == 0:  # Zakładając, że 'h' jest ustawione na 0 dla nowego centralnego węzła
                central_node = node
                break
        self.assertIsNotNone(central_node)
        # self.graph.visualize()

    def test_p4_production_applies_to_rolled_graph(self):
        self.setUpRolledGraph()
        # self.graph.visualize()
        prod = P4()
        results = prod.search_for_subgraphs(self.graph)
        for subgraph in results:
            prod.apply_production(self.graph, subgraph)
            break

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 9  # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 16  # 4 oryginalne krawędzie są podzielone na 8, a do węzła centralnego dodane są 4 nowe krawędzie
        self.assertEqual(self.graph.get_number_of_edges(), expected_num_edges)

        # 3. Sprawdź obecność nowego centralnego węzła i jego właściwości
        central_node = None
        for node in self.graph.get_nodes():
            if node.label == "V" and node.h == 0:  # Zakładając, że 'h' jest ustawione na 0 dla nowego centralnego węzła
                central_node = node
                break
        self.assertIsNotNone(central_node)
        # self.graph.visualize()

    def test_p4_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        # self.graph.visualize()
        prod = P4()
        results = prod.search_for_subgraphs(self.graph)
        for subgraph in results:
            prod.apply_production(self.graph, subgraph)
            break

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 11   # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 18  # 4 oryginalne krawędzie są podzielone na 8, a do węzła centralnego dodane są 4 nowe krawędzie
        self.assertEqual(self.graph.get_number_of_edges(), expected_num_edges)

        # 3. Sprawdź obecność nowego centralnego węzła i jego właściwości
        central_node = None
        for node in self.graph.get_nodes():
            if node.label == "V" and node.h == 0:  # Zakładając, że 'h' jest ustawione na 0 dla nowego centralnego węzła
                central_node = node
                break
        self.assertIsNotNone(central_node)
        # self.graph.visualize()

    def test_p4_production_does_not_apply_because_missing_vertex(self):
        self.setUpIncompleteGraphWithMissingVertex()  # Ustawienie niekompletnego grafu dla tego testu
        # self.incomplete_graph.visualize()
        prod = P4()
        results = list(prod.search_for_subgraphs(self.incomplete_graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana)
        self.assertEqual(len(results), 0)

    def test_p4_production_does_not_apply_because_missing_edge(self):
        self.setUpIncompleteGraphWithMissingEdge()  # Ustawienie grafu z brakującą krawędzią dla tego testu
        # self.missing_edge_graph.visualize()
        prod = P4()
        results = list(prod.search_for_subgraphs(self.missing_edge_graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z brakującą krawędzią)
        self.assertEqual(len(results), 0)

    def test_p4_production_does_not_apply_because_incorrect_R(self):
        self.setUpGraphWithIncorrectR()  # Ustawienie grafu z niepoprawną wartością R dla tego testu
        # self.incorrect_r_graph.visualize()
        prod = P4()
        results = list(prod.search_for_subgraphs(self.incorrect_r_graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z niepoprawną wartością R)
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()
