import sys 

input = sys.stdin.readline 

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

# 그래프에 입력값 넣기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True 
    graph[b][a] = True

q = [V]
visited2[V] = True

def dfs(idx):
    global visited1
    visited1[idx] = True
    print(idx, end = ' ')
    for next in range(1, N + 1):
        if not visited1[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited2
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N + 1):
            if not visited2[next] and graph[cur][next]:
                visited2[next] = True
                q.append(next)


dfs(V)
print()
bfs()














