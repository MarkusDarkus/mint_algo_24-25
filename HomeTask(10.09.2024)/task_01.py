"""Написать все функции преобразований между такими типами хранения невзвешенного графа в памяти, как список смежности, матрица смежности, список ребер.
На вход граф с одним типом хранения, на выходе с другим.
"""

#1. Список смежности в матрицу смежности:
def adjacency_list_to_adjacency_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]
    
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            adj_matrix[i][neighbor] = 1
            
    return adj_matrix
    
#2. Матрица смежности в список смежности:
def adjacency_matrix_to_adjacency_list(adj_matrix):
    adj_list = []
    
    for row in adj_matrix:
        neighbors = [i for i, val in enumerate(row) if val == 1]
        adj_list.append(neighbors)
        
    return adj_list
    
#3. Список смежности в список ребер:
def adjacency_list_to_edge_list(adj_list):
    edge_list = []
    
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            if (neighbor, i) not in edge_list:  # чтобы избежать дубликатов
                edge_list.append((i, neighbor))
                
    return edge_list

#4. Список ребер в список смежности:
def edge_list_to_adjacency_list(edge_list, num_vertices):
    adj_list = [[] for _ in range(num_vertices)]
    
    for u, v in edge_list:
        adj_list[u].append(v)
        adj_list[v].append(u)  # для невзвешенного графа, добавляем обе стороны
        
    return adj_list

#5. Матрица смежности в список ребер:
def adjacency_matrix_to_edge_list(adj_matrix):
    edge_list = []
    n = len(adj_matrix)
    
    for i in range(n):
        for j in range(i + 1, n):  # избегаем дубликатов (u, v) и (v, u)
            if adj_matrix[i][j] == 1:
                edge_list.append((i, j))
                
    return edge_list
    
def edge_list_to_adjacency_matrix(edge_list, num_vertices):
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    for u, v in edge_list:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1  # для невзвешенного графа
        
    return adj_matrix