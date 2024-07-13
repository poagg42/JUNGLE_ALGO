# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000)

import sys 
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

# 방문 리스트 행렬
visited1 = [0] * (N + 1)

# dfs

def dfs(V):
    visited1[V] = 1
    for i in graph[V]:
        if visited1[i] == 0:
            visited1[i] = True
            dfs(i)

count = 0
for i in range(1, N+1):
    if visited1[i] == False:
        count += 1
        dfs(i)

print(count)