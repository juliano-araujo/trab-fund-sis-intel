from graph import graph
import algorithms
import distances
from cities import cities_dict 

def heuristics_gen(route_type: str):
  def heuristics(x: int, y: int):
    if route_type == 'land': 
      return distances.land_route[x][y]
    else:
      return distances.air_route[x][y]
  
  return heuristics


# Busca em largura
# Busca em profundidade
# Busca de custo uniforme
# Busca Gulosa
# Busca A*

def run_algorithms(start: int, goal: int):
  print(f'\n\nRodando algoritmos para encontrar o caminho entre cidades {cities_dict[start]}, {cities_dict[goal]}\n\n')

  path_bfs, nodes_opened_bfs = algorithms.bfs(graph, start, goal)
  generate_texts('Busca em largura', path_bfs, nodes_opened_bfs)

  path_dfs, nodes_opened_dfs = algorithms.dfs(graph, start, goal)
  generate_texts('Busca em profundidade', path_dfs, nodes_opened_dfs)

  path_ucs_air, nodes_opened_ucs_air = algorithms.ucs(graph, 'weight_air', start, goal)
  generate_texts('Busca de custo uniforme usando distância aérea', path_ucs_air, nodes_opened_ucs_air)

  path_ucs_land, nodes_opened_ucs_land = algorithms.ucs(graph, 'weight_land', start, goal)
  generate_texts('Busca de custo uniforme usando distância terrestre', path_ucs_land, nodes_opened_ucs_land)

  path_greedy_air, nodes_opened_greedy_air = algorithms.greedy(graph, heuristics_gen('air'), start, goal)
  generate_texts('Busca Gulosa usando distância aérea', path_greedy_air, nodes_opened_greedy_air)
  
  path_greedy_land, nodes_opened_greedy_land = algorithms.greedy(graph, heuristics_gen('land'), start, goal)
  generate_texts('Busca Gulosa usando distância terrestre', path_greedy_land, nodes_opened_greedy_land)

  path_a_star_air, nodes_opened_a_star_air = algorithms.a_star(graph, 'weight_air', heuristics_gen('air'), start, goal)
  generate_texts('Busca A* usando distância aérea', path_a_star_air, nodes_opened_a_star_air)

  path_a_star_land, nodes_opened_a_star_land = algorithms.a_star(graph, 'weight_land', heuristics_gen('land'), start, goal)
  generate_texts('Busca A* usando distância terrestre', path_a_star_land, nodes_opened_a_star_land)


def generate_texts(algorith_name: str, path: list[int], nodes_opened: int):
    cost_air = algorithms.calculate_weigth_path_between_nodes(graph, 'weight_air', path)
    cost_land = algorithms.calculate_weigth_path_between_nodes(graph, 'weight_land', path)

    path_str = [cities_dict[city] for city in path]
    path_joined = ", ".join(path_str)

    print(f"Os resultados com o algoritmo {algorith_name} foram:\n")
    print(f"O caminho encontrado foi:\n\n{path_joined}")
    print(f"Para chegar nesse caminho foram navegados por {nodes_opened} nós")
    print(f"A distância em terra desse caminho é de: {cost_land}km ")
    print(f"A distância pelo ar desse caminho é de: {cost_air}km ")
    print(f"O caminho com é menor distância é então o pela via { 'aérea' if cost_air < cost_land else 'terrestre'}\n\n")

run_algorithms(2, 5)