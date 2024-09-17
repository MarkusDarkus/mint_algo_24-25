def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = []
    for u in in_degree:
        if in_degree[u] == 0:
            queue.append(u)

    sorted_order = []

    while queue:
        u = queue.pop(0)
        sorted_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(sorted_order) != len(graph):
        return -1

    return sorted_order
