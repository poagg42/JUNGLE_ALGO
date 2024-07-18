import sys 
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [] # 입력받을 그래프를 담을 리스트 선언
result = [] # 결과를 담을 리스트 선언
count = 0

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# def dfs(x, y):
#     global count
#     if x < 0 or x >= N or y < 0 or y >= N:
#         return 
    
#     if graph[x][y] == 1:
#         count += 1
#         graph[x][y] = 0

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)

# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1:
#             dfs(i, j)
#             result.append(count)
#             count = 0

# result.sort()

# print(len(result))
# for k in result:
#     print(k)

def dfs(x, y):
    # global 변수 사용
    global count 
    # 기저조건 설정
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    # 해당 좌표가 True이면
    if graph[x][y] == 1:
        # 카운트 +1
        count += 1
        # 좌표를 0으로 바꾼다.
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# N과 J를 반복하면서
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()

print(len(result))
for k in result:
    print(k)

