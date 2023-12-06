from hypergraph.P1 import P1
from hypergraph.structures import Node, Graph

node1 = Node(0, 0, 3, "one")
node2 = Node(5,0, 1, "two")
node3 = Node(4, 2, 3, "three")
node4 = Node(1, 2, 3, "four")


graph = Graph()

graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
qnode_1 = graph.add_q_node(node1,node2,node3,node4)

enode_1 = graph.add_edge(node1, node2, 1, 2)
enode_2 = graph.add_edge(node2, node3, 3,4)
enode_3 = graph.add_edge(node3, node4, 3,4)
enode_4 = graph.add_edge(node4, node1, 3,4)



nodes = graph.get_nodes()
# first_node = next(iter(nodes))
# label = first_node.label

# print(label)

edges = graph.get_edges()
# print(len(edges))

# print(label)

graph.visualize()

g2 = P1(graph)
g2.visualize()