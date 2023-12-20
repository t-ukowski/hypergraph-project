from hypergraph.structures import Graph, Node, QNode, ENode
import networkx as nx

class ProductionBase:
    def __init__(self):
        self.graph = Graph()
        self.nodes = []
        self.enodes = []
        self.qnode = None
        self.left_graph = None

    def node_match(self, n1, n2):
        raise NotImplementedError("This method should be implemented in a subclass")

    def search_for_subgraphs(self, graph: Graph):
        if self.left_graph is None:
            raise ValueError("Left graph not set")
        return nx.isomorphism.GraphMatcher(graph.G, self.left_graph.G, node_match=self.node_match).subgraph_isomorphisms_iter()

    def apply_production(self, graph, mapping):
        raise NotImplementedError("This method should be implemented in a subclass")
