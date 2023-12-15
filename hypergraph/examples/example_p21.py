from hypergraph.productions.p21 import P21

prod = P21()

graph = prod.graph

graph.visualize()

results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
