from hypergraph.productions import P12

prop = P12()


graph = prop.graph

left_graph = graph

left_graph.visualize()

prod = P12()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
