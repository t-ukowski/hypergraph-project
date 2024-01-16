from ..productions import P14

prop = P14()


graph = prop.graph

left_graph = graph

left_graph.visualize()

prod = P14()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
