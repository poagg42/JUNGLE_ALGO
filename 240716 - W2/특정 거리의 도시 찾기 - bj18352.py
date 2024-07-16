import sys 
from collections import deque

input = sys.stdin.readline

# 도시의 개수 N, 도시의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
q = deque()
q.append(1)


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)




