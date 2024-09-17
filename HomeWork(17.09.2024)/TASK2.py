from collections import defaultdict, deque

def topological_sort(vertices, edges):
    graph = defaultdict(list)
    in_degree = {v: 0 for v in vertices}
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([v for v in vertices if in_degree[v] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(vertices):
        return -1

    return sorted_order

V = ['Пиджак', 'Часы', 'Брюки', 'Рубашка', 'Трусы', 'Носки', 'Туфли', 'Галстук', 'Ремень']
E = [('Галстук', 'Пиджак'), ('Носки', 'Туфли'), ('Рубашка', 'Ремень'), 
     ('Рубашка', 'Галстук'), ('Ремень', 'Пиджак'), ('Трусы', 'Брюки'), 
     ('Трусы', 'Туфли'), ('Брюки', 'Туфли'), ('Брюки', 'Ремень')]

result = topological_sort(V, E)
print(result)
