from hypergraph.productions import P6
from hypergraph.structures import Node, Graph

prod = P6()


graph = prod.graph

left_graph = graph

left_graph.visualize()

prod = P6()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()