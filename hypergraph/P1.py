from hypergraph.structures import Node, Edge

#TODO: Update input params (4 nodes instead of whole graph)
def P1(graph):
    new_nodes = []
    new_edges = []

    x_sum = 0
    y_sum = 0
    for node in graph.get_nodes():
        x_sum += node.x
        y_sum += node.y

    center_x = x_sum / 4
    center_y = y_sum / 4
    center_node = Node(center_x, center_y)
    new_nodes.append(center_node)

    for v1, v2, data in graph.get_edges():
        x1, y1 = v1.x, v1.y
        x2, y2 = v2.x, v2.y

        new_x = (x1 + x2) / 2
        new_y = (y1 + y2) / 2

        new_node = Node(new_x, new_y)
        new_nodes.append(new_node)

        edge_1 = Edge(v1, new_node)
        edge_2 = Edge(v2, new_node)

        new_edges.extend([edge_1, edge_2])

        center_edge = Edge(center_node, new_node)
        new_edges.append(center_edge)

    # TODO: Remove old edges
    for node in new_nodes:
        graph.add_node(node)

    for edge in new_edges:
        graph.add_edge(edge.v1, edge.v2)

    return graph
