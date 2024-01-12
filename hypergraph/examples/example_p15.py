from ..productions import P15

prop = P15()


graph = prop.graph

left_graph = graph

left_graph.visualize()

prod = P15()
results = prod.search_for_subgraphs(graph)
for subgraph in results:
    prod.apply_production(graph, subgraph)
    break

graph.visualize()
