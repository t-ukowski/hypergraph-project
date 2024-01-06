from hypergraph.productions import P10

prop = P10()


graph = prop.graph

left_graph = graph

left_graph.visualize()

prod = P10()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
