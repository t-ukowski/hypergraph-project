from hypergraph.productions import P11

prop = P11()


graph = prop.graph

left_graph = graph

left_graph.visualize()

prod = P11()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
