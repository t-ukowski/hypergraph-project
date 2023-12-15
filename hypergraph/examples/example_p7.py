from hypergraph.productions import P7
from hypergraph.structures import Node, Graph

node1 = Node(0, 0, 0)
node2 = Node(5,0, 0)
node3 = Node(5, 5, 0)
node4 = Node(0, 5, 0)
graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
qnode_1 = graph.add_q_node(node1,node2,node3,node4)

graph.visualize()

prod = P7()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()