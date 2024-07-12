V, E = 6, 8
edge = [0, 1, 0, 2, 0, 5, 0, 6, 4, 3, 5, 3, 5, 4, 6, 4]

adj_matrix = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
        # 2*i와 2*i+1은 edge 리스트에서 간선 정보를 가져오기 위한 인덱스
        num1, num2 = edge[2*i], edge[2*i+1]
        # num1 정점에서 num2 정점으로의 방향성을 가진 간선이 존재함을 나타냄
        adj_matrix[num1][num2] = 1

print(adj_matrix)