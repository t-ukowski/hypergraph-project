from hypergraph.productions.p9 import P9

prod = P9()

graph = prod.graph

graph.visualize()

results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
