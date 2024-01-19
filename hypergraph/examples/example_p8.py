from hypergraph.productions import P8
from hypergraph.structures import Node, Graph

prod = P8()

graph = prod.graph

left_graph = graph

left_graph.visualize()

prod = P8()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()