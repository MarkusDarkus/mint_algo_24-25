def has_odd_cycle(adj_list):
    # Фильтруем нечетные вершины
    odd_vertices = [v for v in range(len(adj_list)) if v % 2 != 0]
    
    # Создаем подграф для нечетных вершин
    odd_graph = {v: [] for v in odd_vertices}
    for v in odd_vertices:
        for neighbor in adj_list[v]:
            if neighbor in odd_vertices:
                odd_graph[v].append(neighbor)

    # Функция для поиска цикла
    def dfs(v, visited, parent):
        visited.add(v)
        for neighbor in odd_graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True
        return False

    # Проверяем каждый нечетный узел
    visited = set()
    for v in odd_vertices:
        if v not in visited:
            if dfs(v, visited, -1):
                return True
    return False


adj_list = [
    [1, 2],     
    [0, 2],     
    [0],        
    [1, 4],    
    [3]         
]

print(has_odd_cycle(adj_list)) 
adj_list = [
    [1, 2],     
    [0, 3],     
    [0],        
    [1, 4],    
    [3]         
]
print(has_odd_cycle(adj_list)) 