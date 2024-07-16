import sys 
from collections import deque

input = sys.stdin.readline 

graph = []

N, M = map(int,(input().split()))

for _ in range(N):
    graphList = list(map(int, input().rstrip()))
    graph.append(graphList)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

# 1. 큐를 이용해 진행한다. 큐에 시작 좌표를 넣는다.

# 2. q에서 꺼낸다. x,y에 popleft한 값을 넣는다.

# 3. 동서남북 반복

# 4. 전체 행렬 이내고 위치값이 1이라면 좌표를 queue에 추가한다.

# 5. 최종 좌표 반환

def bfs(x, y):

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


    return graph[N - 1][M - 1]

print(bfs(0,0))            
