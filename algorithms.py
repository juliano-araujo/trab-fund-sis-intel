from collections import deque
import networkx as nx
import heapq
from typing import Callable

def calculate_weigth_path_between_nodes(graph: nx.Graph, param_name: str, path: list[int]) -> int:
    total_weight = 0
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        weight = graph.edges[u, v].get(param_name, 1)
        total_weight += weight

    return total_weight

def bfs(graph: nx.Graph, start: int, goal: int):
    visited = set()  
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                new_path = path + [neighbor]
                visited.add(neighbor)
                # print(f"visitou {neighbor} -> path {new_path}")

                if neighbor == goal:
                  return new_path, len(visited)
                
                queue.append((neighbor, new_path))

    return None, len(visited)

def dfs(graph: nx.Graph, start: int, goal: int):
    visited = set()  
    stack =[(start, [start])]
    while len(stack) > 0:
        node, path = stack.pop()

        if node in visited:
          continue
        
        visited.add(node)
        # print(f"visitou {node} -> path {path}")
        
        if node == goal:
          return path, len(visited)
        
        for neighbor in graph.neighbors(node):
            stack.append((neighbor, path + [neighbor]))

    return None, len(visited)


def ucs(graph: nx.Graph, param_name: str, start: int, goal: int):
    visited = set()
    heap = [(0, start, [start])]

    while heap:
        cost, node, path = heapq.heappop(heap)

        if node == goal:
            return path, len(visited)

        if node in visited:
            continue

        visited.add(node)                
        # print(f"visitou {node} -> path: {path} cost: {cost}")

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                edge_weight = graph.edges[node, neighbor].get(param_name, 1)
                heapq.heappush(heap, (cost + edge_weight, neighbor, path + [neighbor]))

    return None, len(visited)

def greedy(graph: nx.Graph, heuristic_function: Callable[[int, int], int] ,start: int, goal: int):
    visited = set()
    node_heuristic = heuristic_function(start, goal)
    heap = [(node_heuristic, start, [start])]

    while heap:
        heuristic, node, path = heapq.heappop(heap)

        if node == goal:
            return path, len(visited)

        if node in visited:
            continue

        visited.add(node)                
        # print(f"visitou {node} -> path: {path} heuristic: {heuristic}")

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                neighbor_heuristic = heuristic_function(neighbor, goal)
                heapq.heappush(heap, (neighbor_heuristic, neighbor, path + [neighbor]))

    return None, len(visited)

def a_star(graph: nx.Graph,  param_name: str, heuristic_function: Callable[[int, int], int] ,start: int, goal: int):
    visited = set()
    node_heuristic = heuristic_function(start, goal)
    heap = [(node_heuristic, 0, start, [start])]

    while heap:
        heuristic, cost, node, path = heapq.heappop(heap)

        if node == goal:
            return path, len(visited)

        if node in visited:
            continue

        visited.add(node)                
        # print(f"visitou {node} -> path: {path} heuristic: {heuristic}")

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                edge_weight = graph.edges[node, neighbor].get(param_name, 1)
                new_cost = cost + edge_weight
                neighbor_heuristic = new_cost + heuristic_function(neighbor, goal)
                heapq.heappush(heap, (neighbor_heuristic, new_cost, neighbor, path + [neighbor]))

    return None, len(visited)