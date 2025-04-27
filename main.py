from graph import graph
import algorithms
import distances

def heuristics_gen(route_type: str):
  def heuristics(x: int, y: int):
    if route_type == 'land': 
      return distances.land_route[x][y]
    else:
      return distances.air_route[x][y]
  
  return heuristics

path, nodes_opened = algorithms.bfs(graph, 14, 9)
path, nodes_opened = algorithms.dfs(graph, 14, 9)
path, nodes_opened = algorithms.ucs(graph, 'weight_air', 14, 9)
path, nodes_opened = algorithms.greedy(graph, heuristics_gen('air'), 14, 9)
path, nodes_opened = algorithms.a_star(graph, 'weight_air',heuristics_gen('air'), 14, 9)



print(f"path {path}")
print(f"nodes opened {nodes_opened}")
