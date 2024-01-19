from hypergraph.productions import P6, P7
from hypergraph.structures import Node, Graph


def step1(graph):
    
    # square nodes
    square_nodes = [
        Node(0, 0, 0),
        Node(10, 0, 0),
        Node(10, 5, 0),
        Node(10, 10, 0),
        Node(0, 10, 0),
        Node(0, 5, 0),
    ]
    
    # hexagon nodes
    hexagon_nodes = [
        Node(3, 2, 0),
        Node(7, 2, 0),
        Node(8, 5, 0),
        Node(7, 7, 0),
        Node(3, 7, 0),
        Node(2, 5, 0),
    ]
        
    for node in square_nodes:
        graph.add_node(node)
        
    for node in hexagon_nodes:
        graph.add_node(node)
        
    for (node1, node2) in zip(square_nodes, hexagon_nodes):
        graph.add_edge(node1, node2)
        
    for i in range(0, 6):
        graph.add_edge(square_nodes[i], square_nodes[(i + 1) % 6])
        
    for i in range(0, 6):    
        graph.add_edge(hexagon_nodes[i], hexagon_nodes[(i + 1) % 6])
    
    s_node = graph.add_s_node(*hexagon_nodes)
    for i in range(0, 6):
        graph.add_q_node(square_nodes[i], square_nodes[(i + 1) % 6], hexagon_nodes[i], hexagon_nodes[(i + 1) % 6])
    
    return graph


def step2(graph):
    prod = P7()
    for i, subgraph in enumerate(prod.search_for_subgraphs(graph)):
        if i == 2:
            print(subgraph.values())
        # prod.apply_production(graph, subgraph)
    return graph


if __name__ == "__main__":
    
    graph = Graph()

    graph = step1(graph)
    print(graph)
    graph.visualize()
    graph = step2(graph)
    graph.visualize()

    ##############################
    