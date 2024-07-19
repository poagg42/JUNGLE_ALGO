from collections import deque

visited = [False] * 9

graph = [
    [],
    [2, 5],
    [3, 4],
    [],
    [],
    [6, 7],
    [],
    []
]

# BFS
def BFS(graph, start, visited):
    # 큐에 탐색을 시작할 노드 넣기
    queue = deque([start])
    # 시작 노드 방문 표시
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 제일 먼저 들어온 것을 꺼낸다.
        v = queue.popleft()
        # 현재 노드 출력
        print(v, end = ' ')

        # 인접 노드 확인
        for i in graph[v]:
            # 만약 인접 노드를 방문하지 않았다면
            if not visited[i]:
                # 큐에 인접 노드 추가하기
                queue.append(i)
                # 인접 노드 방문 표시
                visited[i] = True


# BFS 실행
BFS(graph, 1, visited)
