from hypergraph.productions import P1, P2, P3, P7, P8, P9, P21
from hypergraph.structures import Node, Graph, SNode, ENode, QNode


def initialize(square_nodes, hexagon_nodes):
    graph = Graph()

    for node in square_nodes:
        graph.add_node(node)

    for node in hexagon_nodes:
        graph.add_node(node)

    for node1, node2 in zip(square_nodes, hexagon_nodes):
        graph.add_edge(node1, node2)

    for i in range(0, 6):
        graph.add_edge(square_nodes[i], square_nodes[(i + 1) % 6])

    for i in range(0, 6):
        graph.add_edge(hexagon_nodes[i], hexagon_nodes[(i + 1) % 6])

    graph.add_s_node(*hexagon_nodes)
    for i in range(0, 6):
        graph.add_q_node(
            square_nodes[i],
            square_nodes[(i + 1) % 6],
            hexagon_nodes[i],
            hexagon_nodes[(i + 1) % 6],
        )

    return graph


def format_requirements(requirements):
    return [str(requirement) for requirement in requirements]


def is_matching_requirements(subgraph, requirements):
    return all(str(v) in requirements for v in subgraph)


def apply_production(graph, prod, requirements):
    requirements = format_requirements(requirements)
    for _, subgraph in enumerate(prod.search_for_subgraphs(graph)):
        if is_matching_requirements(subgraph, requirements):
            prod.apply_production(graph, subgraph)
            break
    else:
        raise ValueError("No subgraph found")
    return graph


if __name__ == "__main__":
    square_nodes = [
        Node(0, 0, 0),
        Node(10, 0, 0),
        Node(10, 5, 0),
        Node(10, 10, 0),
        Node(0, 10, 0),
        Node(0, 5, 0),
    ]

    hexagon_nodes = [
        Node(3, 2, 0),
        Node(7, 2, 0),
        Node(8, 5, 0),
        Node(7, 7, 0),
        Node(3, 7, 0),
        Node(2, 5, 0),
    ]

    graph = initialize(square_nodes, hexagon_nodes)
    graph.visualize()
    graph = apply_production(
        graph,
        P21(),
        [
            *hexagon_nodes,
            SNode(
                x=sum([node.x for node in hexagon_nodes]) / 6,
                y=sum([node.y for node in hexagon_nodes]) / 6,
            ),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P9(),
        [
            *hexagon_nodes,
            SNode(
                x=sum([node.x for node in hexagon_nodes]) / 6,
                y=sum([node.y for node in hexagon_nodes]) / 6,
                R=1,
            ),
            *[
                ENode(
                    x=coords[0],
                    y=coords[1],
                )
                for coords in [
                    (2.5, 3.5),
                    (5.0, 2.0),
                    (7.5, 3.5),
                    (7.5, 6.0),
                    (5.0, 7.0),
                    (2.5, 6.0),
                ]
            ],
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P7(h1=1, h2=1),
        [
            Node(8, 5),
            Node(7.5, 3.5, 1),
            Node(7.5, 6.0, 1),
            Node(5.0, 4.666666666666667),
            QNode(7.0, 4.791666666666667),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P8(h7=1),
        [
            Node(10, 10),
            QNode(8.75, 6.75),
            Node(7, 7),
            Node(8, 5),
            Node(10, 5),
            QNode(7.0, 4.791666666666667, 1),
            Node(7.5, 6.0, 1),
            Node(5.0, 4.666666666666667),
            Node(7.5, 3.5, 1),
            ENode(7.25, 6.5),
            ENode(7.75, 5.5),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P8(h7=1),
        [
            Node(10, 0),
            QNode(8.75, 3.0),
            Node(7, 2),
            Node(8, 5),
            Node(10, 5),
            QNode(7.0, 4.791666666666667, 1),
            Node(7.5, 3.5, 1),
            Node(5.0, 4.666666666666667),
            Node(7.5, 6.0, 1),
            ENode(7.25, 2.75),
            ENode(7.75, 4.25),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P2(),
        [
            Node(10, 5),
            QNode(8.75, 6.75, 1),
            Node(8, 5),
            Node(7, 7),
            Node(10, 10),
            ENode(9.0, 5.0),
            ENode(7.75, 5.5),
            Node(7.5, 6.0, 1),
            ENode(7.25, 6.5),
            ENode(8.5, 8.5),
            ENode(10.0, 7.5),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P3(),
        [
            Node(10, 5),
            QNode(8.75, 3.0, 1),
            Node(8, 5),
            Node(7, 2),
            Node(10, 0),
            ENode(9.5, 5.0),
            Node(9.0, 5.0, 1),
            ENode(8.5, 5.0),
            ENode(7.75, 4.25),
            Node(7.5, 3.5, 1),
            ENode(7.25, 2.75),
            ENode(8.5, 1.0),
            ENode(10.0, 2.5),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P1(),
        [
            Node(8, 5),
            QNode(7.0, 4.791666666666667, 1),
            Node(7.5, 3.5),
            Node(5.0, 4.666666666666667),
            Node(7.5, 6.0),
            ENode(7.75, 4.25),
            ENode(6.25, 4.083333333333334),
            ENode(6.25, 5.333333333333334),
            ENode(7.75, 5.5),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P7(h1=1, h2=1),
        [
            Node(7.75, 5.5, 1),
            QNode(7.625, 4.885416666666667),
            Node(7.75, 4.25, 1),
            Node(8, 5),
            Node(7.0, 4.791666666666667),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P8(h7=1),
        [
            Node(8.75, 3.0),
            QNode(8.3125, 4.125),
            Node(7.5, 3.5),
            Node(8, 5),
            Node(9.0, 5.0),
            QNode(7.625, 4.885416666666667, 1),
            Node(7.75, 4.25, 1),
            Node(7.0, 4.791666666666667),
            Node(7.75, 5.5, 1),
            ENode(7.625, 3.875),
            ENode(7.875, 4.625),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P8(h7=1),
        [
            Node(8.75, 6.75),
            QNode(8.3125, 5.6875),
            Node(7.5, 6.0),
            Node(8, 5),
            Node(9.0, 5.0),
            QNode(7.625, 4.885416666666667, 1),
            Node(7.75, 5.5, 1),
            Node(7.0, 4.791666666666667),
            Node(7.75, 4.25, 1),
            ENode(7.625, 5.75),
            ENode(7.875, 5.25),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P2(),
        [
            Node(9.0, 5.0),
            QNode(8.3125, 5.6875, 1),
            Node(8, 5),
            Node(7.5, 6.0),
            Node(8.75, 6.75),
            ENode(8.5, 5.0),
            ENode(7.875, 5.25),
            Node(7.75, 5.5, 1),
            ENode(7.625, 5.75),
            ENode(8.125, 6.375),
            ENode(8.875, 5.875),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P3(),
        [
            Node(9.0, 5.0),
            QNode(8.3125, 4.125, 1),
            Node(8, 5),
            Node(7.5, 3.5),
            Node(8.75, 3.0),
            ENode(8.75, 5.0),
            Node(8.5, 5.0, 1),
            ENode(8.25, 5.0),
            ENode(7.875, 4.625),
            Node(7.75, 4.25, 1),
            ENode(7.625, 3.875),
            ENode(8.125, 3.25),
            ENode(8.875, 4.0),
        ],
    )
    graph.visualize()
    graph = apply_production(
        graph,
        P1(),
        [
            Node(8, 5),
            QNode(7.625, 4.885416666666667, 1),
            Node(7.75, 4.25),
            Node(7.0, 4.791666666666667),
            Node(7.75, 5.5),
            ENode(7.875, 4.625),
            ENode(7.375, 4.520833333333334),
            ENode(7.375, 5.145833333333334),
            ENode(7.875, 5.25),
        ],
    )
    graph.visualize()
