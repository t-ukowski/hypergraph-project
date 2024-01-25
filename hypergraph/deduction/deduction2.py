from hypergraph.productions import P1, P2, P7, P8
from hypergraph.structures import Node, Graph, QNode


def create_graph():
    """
    Tworzy graf z predefiniowanymi węzłami i krawędziami.
    """

    # Inicjalizacja węzłów
    nodes = [Node(0, 0, 0), Node(10, 0, 0), Node(10, 5, 0), Node(10, 10, 0),
             Node(0, 10, 0), Node(0, 5, 0), Node(3, 2, 0), Node(7, 2, 0),
             Node(8, 5, 0), Node(7, 8, 0), Node(3, 8, 0), Node(2, 5, 0)]

    # Tworzenie grafu i dodawanie węzłów
    graph = Graph()
    for node in nodes:
        graph.add_node(node)

    # Dodawanie krawędzi zewnętrznych
    outer_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]

    # Dodawanie krawędzi wewnętrznych
    inner_edges = [(6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 6)]

    # Dodawanie krawędzi łączących zewnętrzne i wewnętrzne węzły
    connecting_edges = [(0, 6), (1, 7), (2, 8), (3, 9), (4, 10), (5, 11)]

    # Dodawanie wszystkich krawędzi do grafu
    for start, end in inner_edges + connecting_edges:
        graph.add_edge(nodes[start], nodes[end])
    for start, end in outer_edges:
        graph.add_edge(nodes[start], nodes[end], 1)
    # Dodawanie węzłów Q i S
    for i in range(6):
        graph.add_q_node(nodes[i], nodes[(i + 1) % 6], nodes[i + 6], nodes[(i + 1) % 6 + 6])
    graph.add_s_node(*nodes[6:])

    return graph

def check_qnode_id(subgraph, target_id):
    for node in subgraph.keys():
        if isinstance(node, QNode):
            if node.id == target_id:
                return True
    return False

def check_subgraph_and_apply_production(graph, production, id):
    """
    Aplikuje wybraną produkcję na grafie.

    :param graph: Graf, na którym będzie stosowana produkcja.
    :param production: Rodzaj produkcji do zastosowania (np. P7).
    """

    prod = production()
    results = prod.search_for_subgraphs(graph)

    for subgraph in results:
        if check_qnode_id(subgraph, target_id=id):
            prod.apply_production(graph, subgraph)
            break



graph = create_graph()
graph.visualize()


id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P7, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P1, id)
graph.visualize()


id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P7, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P8, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P2, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P1, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P7, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P8, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P2, id)
graph.visualize()

id = int(input("Podaj ID podgrafu: "))
check_subgraph_and_apply_production(graph, P1, id)
graph.visualize()
#
