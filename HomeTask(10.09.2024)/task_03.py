def is_reachable(graph, start, end):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    
    return False

def are_vertices_mutually_reachable(graph, v, u):
    return is_reachable(graph, v, u) and is_reachable(graph, u, v)

# Пример использования:
graph = {
    0: [1],
    1: [2],
    2: [0],
    3: [4],
    4: []
}

v = 0
u = 2
print(are_vertices_mutually_reachable(graph, v, u))  # True

v = 3
u = 4
print(are_vertices_mutually_reachable(graph, v, u))  # False