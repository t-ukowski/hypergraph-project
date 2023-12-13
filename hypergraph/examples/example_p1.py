from ..productions import P1
from hypergraph.structures import Node, Graph

node1 = Node(0, 0, 0)
node2 = Node(5, 0, 0)
node3 = Node(5, 5, 0)
node4 = Node(0, 5, 0)
graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
qnode_1 = graph.add_q_node(node1, node2, node3, node4)
qnode_1.R = 1
enode_1 = graph.add_edge(node1, node2)
enode_2 = graph.add_edge(node2, node3)
enode_3 = graph.add_edge(node3, node4)
enode_4 = graph.add_edge(node4, node1)
graph.visualize()

prod = P1()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
