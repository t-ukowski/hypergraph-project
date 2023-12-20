import unittest
from hypergraph.structures import Node, Graph
from hypergraph.productions.p1 import P1

class TestP1Production(unittest.TestCase):
    def setUpCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p1_production_applies)
        self.node1 = Node(0, 0, 0)
        self.node2 = Node(2, 0, 0)
        self.node3 = Node(2, 2, 0)
        self.node4 = Node(0, 2, 0)
        self.graph = Graph()
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_node(self.node3)
        self.graph.add_node(self.node4)
        self.qnode = self.graph.add_q_node(self.node1, self.node2, self.node3, self.node4)
        self.qnode.R = 1
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node2, self.node3)
        self.graph.add_edge(self.node3, self.node4)
        self.graph.add_edge(self.node4, self.node1)

    def setUpLargerCompleteGraph(self):
        # Ustawienie dla kompletnego grafu (używane w teście test_p1_production_applies_to_larger_graph)
        self.node1 = Node(0, 0, 0)
        self.node2 = Node(2, 0, 0)
        self.node3 = Node(2, 2, 0)
        self.node4 = Node(0, 2, 0)
        self.node5 = Node(4, 4, 0)
        self.graph = Graph()
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_node(self.node3)
        self.graph.add_node(self.node4)
        self.graph.add_node(self.node5)
        self.qnode = self.graph.add_q_node(self.node1, self.node2, self.node3, self.node4)
        self.qnode.R = 1
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node2, self.node3)
        self.graph.add_edge(self.node3, self.node4)
        self.graph.add_edge(self.node4, self.node1)
        self.graph.add_edge(self.node3, self.node5)

    def setUpIncompleteGraphWithMissingVertex(self):
        # Ustawienie dla niekompletnego grafu (używane w teście test_p1_production_does_not_apply_because_missing_vertex)
        self.incomplete_node1 = Node(0, 0, 0)
        self.incomplete_node2 = Node(2, 0, 0)
        self.incomplete_node3 = Node(2, 2, 0)
        self.incomplete_graph = Graph()
        self.incomplete_graph.add_node(self.incomplete_node1)
        self.incomplete_graph.add_node(self.incomplete_node2)
        self.incomplete_graph.add_node(self.incomplete_node3)
        self.incomplete_graph.add_edge(self.incomplete_node1, self.incomplete_node2)
        self.incomplete_graph.add_edge(self.incomplete_node2, self.incomplete_node3)
        # Celowo pomijamy czwarty węzeł i jego krawędzie

    def setUpIncompleteGraphWithMissingEdge(self):
        # Ustawienie dla grafu z brakującą krawędzią (używane w teście test_p1_production_does_not_apply_because_missing_edge)
        self.missing_edge_node1 = Node(0, 0, 0)
        self.missing_edge_node2 = Node(2, 0, 0)
        self.missing_edge_node3 = Node(2, 2, 0)
        self.missing_edge_node4 = Node(0, 2, 0)
        self.missing_edge_graph = Graph()
        self.missing_edge_graph.add_node(self.missing_edge_node1)
        self.missing_edge_graph.add_node(self.missing_edge_node2)
        self.missing_edge_graph.add_node(self.missing_edge_node3)
        self.missing_edge_graph.add_node(self.missing_edge_node4)
        self.missing_edge_qnode = self.missing_edge_graph.add_q_node(self.missing_edge_node1, self.missing_edge_node2, self.missing_edge_node3, self.missing_edge_node4)
        self.missing_edge_qnode.R = 1
        self.missing_edge_graph.add_edge(self.missing_edge_node1, self.missing_edge_node2)
        self.missing_edge_graph.add_edge(self.missing_edge_node2, self.missing_edge_node3)
        # Celowo pomijamy krawędź między node3 a node4

    
    def setUpGraphWithIncorrectR(self):
        # Ustawienie dla grafu z niepoprawną wartością R (używane w teście test_p1_production_does_not_apply_because_incorrect_R)
        self.incorrect_r_node1 = Node(0, 0, 0)
        self.incorrect_r_node2 = Node(2, 0, 0)
        self.incorrect_r_node3 = Node(2, 2, 0)
        self.incorrect_r_node4 = Node(0, 2, 0)
        self.incorrect_r_graph = Graph()
        self.incorrect_r_graph.add_node(self.incorrect_r_node1)
        self.incorrect_r_graph.add_node(self.incorrect_r_node2)
        self.incorrect_r_graph.add_node(self.incorrect_r_node3)
        self.incorrect_r_graph.add_node(self.incorrect_r_node4)
        self.incorrect_r_qnode = self.incorrect_r_graph.add_q_node(self.incorrect_r_node1, self.incorrect_r_node2, self.incorrect_r_node3, self.incorrect_r_node4)
        self.incorrect_r_qnode.R = 0  # Ustawienie R na niepoprawną wartość
        self.incorrect_r_graph.add_edge(self.incorrect_r_node1, self.incorrect_r_node2)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node2, self.incorrect_r_node3)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node3, self.incorrect_r_node4)
        self.incorrect_r_graph.add_edge(self.incorrect_r_node4, self.incorrect_r_node1)

    # def setUpGraphWithIncorrectCoordinates(self):
    #     # Ustawienie dla grafu z niepoprawnymi współrzędnymi (używane w teście test_p1_production_does_not_apply_because_incorrect_coordinates)
    #     self.incorrect_coord_node1 = Node(0, 0, 0)
    #     self.incorrect_coord_node2 = Node(4, 0, 0)
    #     self.incorrect_coord_node3 = Node(0, 4, 0)  # Niepoprawne współrzędne
    #     self.incorrect_coord_node4 = Node(4, 4, 0)
    #     self.incorrect_coord_graph = Graph()
    #     self.incorrect_coord_graph.add_node(self.incorrect_coord_node1)
    #     self.incorrect_coord_graph.add_node(self.incorrect_coord_node2)
    #     self.incorrect_coord_graph.add_node(self.incorrect_coord_node3)
    #     self.incorrect_coord_graph.add_node(self.incorrect_coord_node4)
    #     self.incorrect_coord_qnode = self.incorrect_coord_graph.add_q_node(self.incorrect_coord_node1, self.incorrect_coord_node2, self.incorrect_coord_node3, self.incorrect_coord_node4)
    #     self.incorrect_coord_qnode.R = 1
    #     self.incorrect_coord_graph.add_edge(self.incorrect_coord_node1, self.incorrect_coord_node2)
    #     self.incorrect_coord_graph.add_edge(self.incorrect_coord_node2, self.incorrect_coord_node3)
    #     self.incorrect_coord_graph.add_edge(self.incorrect_coord_node3, self.incorrect_coord_node4)
    #     self.incorrect_coord_graph.add_edge(self.incorrect_coord_node4, self.incorrect_coord_node1)



    def test_p1_production_applies(self):
        self.setUpCompleteGraph()
        prod = P1()
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

    def test_p1_production_applies_to_larger_graph(self):
        self.setUpLargerCompleteGraph()
        prod = P1()
        results = prod.search_for_subgraphs(self.graph)
        for subgraph in results:
            prod.apply_production(self.graph, subgraph)
            break

        # Aserty
        # 1. Sprawdź liczbę węzłów
        expected_num_nodes = 10  # Dodano jeden nowy węzeł w centrum
        self.assertEqual(self.graph.get_number_of_nodes(), expected_num_nodes)

        # 2. Sprawdź liczbę krawędzi
        expected_num_edges = 17  # 4 oryginalne krawędzie są podzielone na 8, a do węzła centralnego dodane są 4 nowe krawędzie
        self.assertEqual(self.graph.get_number_of_edges(), expected_num_edges)

        # 3. Sprawdź obecność nowego centralnego węzła i jego właściwości
        central_node = None
        for node in self.graph.get_nodes():
            if node.label == "V" and node.h == 0:  # Zakładając, że 'h' jest ustawione na 0 dla nowego centralnego węzła
                central_node = node
                break
        self.assertIsNotNone(central_node)

    def test_p1_production_does_not_apply_because_missing_vertex(self):
        self.setUpIncompleteGraphWithMissingVertex()  # Ustawienie niekompletnego grafu dla tego testu
        prod = P1()
        results = list(prod.search_for_subgraphs(self.incomplete_graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana)
        self.assertEqual(len(results), 0)
        
    def test_p1_production_does_not_apply_because_missing_edge(self):
        self.setUpIncompleteGraphWithMissingEdge()  # Ustawienie grafu z brakującą krawędzią dla tego testu
        prod = P1()
        results = list(prod.search_for_subgraphs(self.missing_edge_graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z brakującą krawędzią)
        self.assertEqual(len(results), 0)

    def test_p1_production_does_not_apply_because_incorrect_R(self):
        self.setUpGraphWithIncorrectR()  # Ustawienie grafu z niepoprawną wartością R dla tego testu
        prod = P1()
        results = list(prod.search_for_subgraphs(self.incorrect_r_graph))

        # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z niepoprawną wartością R)
        self.assertEqual(len(results), 0)
    
    # def test_p1_production_does_not_apply_because_incorrect_coordinates(self):
    #     self.setUpGraphWithIncorrectCoordinates()  # Ustawienie grafu z niepoprawnymi współrzędnymi dla tego testu
    #     prod = P1()
    #     results = list(prod.search_for_subgraphs(self.incorrect_coord_graph))

    #     # Sprawdź, czy nie znaleziono podgrafów (produkcja nie powinna być stosowana z niepoprawnymi współrzędnymi)
    #     self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()
