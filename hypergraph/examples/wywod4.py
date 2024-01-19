from ..productions import *
from hypergraph.structures import Graph, Node

square_nodes = [
    # square
    Node(0, 0, 0),
    Node(6, 0, 0),
    Node(6, 2, 0),
    Node(6, 4, 0),
    Node(0, 4, 0),
    Node(0, 2, 0),
]

hexagon_nodes = [
    # hexagon
    Node(2, 1, 0),
    Node(4, 1, 0),
    Node(5, 2, 0),
    Node(4, 3, 0),
    Node(2, 3, 0),
    Node(1, 2, 0),
]

all_nodes = square_nodes + hexagon_nodes

graph = Graph()

for node in all_nodes:
    graph.add_node(node)

s_node = graph.add_s_node(*hexagon_nodes)

square_edges = {}
# add edges between square nodes 
for n1, n2 in zip(square_nodes, square_nodes[1:] + [square_nodes[0]]):
    square_edges[(n1, n2)] = graph.add_edge(n1, n2, B=1)
    square_edges[(n2, n1)] = square_edges[(n1, n2)]

hexagon_edges = {}
# add edges between hexagon nodes
for n1, n2 in zip(hexagon_nodes, hexagon_nodes[1:] + [hexagon_nodes[0]]):
    hexagon_edges[(n1, n2)] = graph.add_edge(n1, n2, B=0)
    hexagon_edges[(n2, n1)] = hexagon_edges[(n1, n2)]


in_between_edges = {}
# add edges between square and hexagon nodes
for n1, n2 in zip(square_nodes, hexagon_nodes):
    in_between_edges[(n1, n2)] = graph.add_edge(n1, n2, B=0)
    in_between_edges[(n2, n1)] = in_between_edges[(n1, n2)]

q_nodes = []
# add q-nodes
for i in range(6):
    q_nodes.append(graph.add_q_node(
        square_nodes[i],
        hexagon_nodes[i],
        hexagon_nodes[(i + 1) % 6],
        square_nodes[(i + 1) % 6],
    ))

important_vertex = hexagon_nodes[3]
curr_q_node = q_nodes[2]

# graph.visualize()

def find_nearest_q_node(graph, x, y):
    best = Node(100000, 10000000)
    for node in graph.G.nodes():
        if node.label == "Q":
            if (node.x - x) ** 2 + (node.y - y) ** 2 < (best.x - x) ** 2 + (best.y - y) ** 2:
                best = node
    
    return best

def apply_prod(graph, prod):
    for res in prod.search_for_subgraphs(graph):
        prod.apply_production(graph, res)
        break
        


prod = P7()

results = prod.search_for_subgraphs(graph)
for res in results:
    if q_nodes[2] in res:
        prod.apply_production(graph, res)
        break

# graph.visualize()

apply_prod(graph, P1())

# graph.visualize()

next_coords = (curr_q_node.x + important_vertex.x) / 2, (curr_q_node.y + important_vertex.y) / 2

prod = P7()

curr_q_node = find_nearest_q_node(graph, *next_coords)
next_coords = (curr_q_node.x + important_vertex.x) / 2, (curr_q_node.y + important_vertex.y) / 2

for res in prod.search_for_subgraphs(graph):
    print(f"found {res}")
    if curr_q_node in res:
        print("applied")
        prod.apply_production(graph, res)
        break

# graph.visualize()

apply_prod(graph, P8())

apply_prod(graph, P22())

graph.visualize()

apply_prod(graph, P10()) # P10 nie ma

graph.visualize()

apply_prod(graph, P3())

graph.visualize()

apply_prod(graph, P1())

graph.visualize()

curr_q_node = find_nearest_q_node(graph, *next_coords)
next_coords = (curr_q_node.x + important_vertex.x) / 2, (curr_q_node.y + important_vertex.y) / 2

prod = P7()
for res in prod.search_for_subgraphs(graph):
    if curr_q_node in res:
        prod.apply_production(graph, res)
        break

graph.visualize()

apply_prod(graph, P8())
apply_prod(graph, P8())

graph.visualize()

apply_prod(graph, P2())

graph.visualize()

apply_prod(graph, P3())

graph.visualize()

apply_prod(graph, P1())

graph.visualize()