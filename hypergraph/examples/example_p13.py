from ..productions import P13

prop = P13()


graph = prop.graph

left_graph = graph

left_graph.visualize()

prod = P13()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
