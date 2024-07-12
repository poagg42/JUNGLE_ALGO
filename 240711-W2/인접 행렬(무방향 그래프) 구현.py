V, E = 6, 8
edge = [0, 1, 0, 2, 0, 5, 0, 6, 4, 3, 5, 3, 5, 4, 6, 4]

adj_matrix = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    num1, num2 = edge[2*i], edge[2*i+1]
    adj_matrix[num1][num2] = 1
    adj_matrix[num2][num1] = 1

print(adj_matrix)