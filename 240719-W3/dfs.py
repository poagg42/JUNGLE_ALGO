# DFS

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

def DFS(graph, v, visited):
	
    # 방문 처리
    visited[v] = True
    # 현재 노드 출력
    print(v, end = ' ')
	
    # 인접 노드 확인
    for i in graph[v]:
    	# 만약 인접노드를 방문하지 않았다면
        if not visited[i]:
        	# 인접 노드 탐색
            DFS(graph, i, visited)
            
            
# DFS 실행
DFS(graph, 1, visited)