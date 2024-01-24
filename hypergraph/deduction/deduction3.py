from hypergraph.productions import P6, P7, P1, P8
from hypergraph.structures import Node, Graph
import numpy as np


class Pivot:
    def __init__(self, o, a, b, c):
        self.o = o
        self.Ms = [
            np.linalg.inv(np.array([a - o, b - o])),
            np.linalg.inv(np.array([b - o, c - o])),
            np.linalg.inv(np.array([c - o, a - o])),
        ]
        
    def is_between(self, x, idx: int):
        x = x - self.o
        x = x @ self.Ms[idx]
        return (x[0] >= 0) and (x[1] >= 0)


# best_subgraph = None
# best_dist = 1e6
# idx = 0 # 1, 2
# for subgraph in production:
#     q_node = np.array(subgraph.q_node.pos)
#     if not pivot.is_between(q_node, idx):
#         continue
#     dist = np.linalg.norm(q_node - pivot.o)
#     if dist < best_dist:
#         best_dist = dist
#         best_subgraph = subgraph

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
    
    pivot = Pivot(np.array([7, 7]), np.array([8, 5]), np.array([10, 10]), np.array([3, 7]))
        
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
    
    return graph, pivot


def step2(graph, pivot, idx, prod):
    best_subgraph = None
    best_dist = 1e6
    for subgraph in prod.search_for_subgraphs(graph):
        qnode = None
        for node in subgraph:
            if node.label == "Q":
                qnode = node
                break
        q_node = np.array([qnode.x, qnode.y])
        if not pivot.is_between(q_node, idx):
            continue
        dist = np.linalg.norm(q_node - pivot.o)
        if dist < best_dist:
            best_dist = dist
            best_subgraph = subgraph
    prod.apply_production(graph, best_subgraph)
    return graph

def step3(graph, prod):
    for subgraph in prod.search_for_subgraphs(graph):
        for node in subgraph:
            print(node.x, node.y)
        prod.apply_production(graph, subgraph)
        break
    
    return graph


if __name__ == "__main__":
    
    graph = Graph()

    graph, pivot = step1(graph)
    graph.visualize()
    
    graph = step2(graph, pivot, idx=0, prod=P7())
    graph.visualize()
    
    graph = step3(graph, prod=P1())
    graph.visualize()
    
    graph = step2(graph, pivot, idx=0, prod=P7())
    graph.visualize()
    
    graph = step3(graph, prod=P8())
    graph.visualize()
    
    

    ##############################
    