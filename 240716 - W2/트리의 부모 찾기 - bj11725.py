"""
트리의 부모 찾기
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	87089	39025	27414	42.542%
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6

"""

import sys 
from collections import deque
input = sys.stdin.readline

# 정점의 수
N = int(input())
# 연결 정보를 저장할 link list의 배열
vertices = [[0] for _ in range(N + 1)]
# 부모를 기록하는 배열
parent = [0] * (N + 1)

# 두 정점간의 연결 정보 저장
for _ in range(N - 1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)

parent[1] = 0
q = deque()
q.append(1)

# queue가 비어있지 않으면 반복
while q:
    # q에서 팝한 것을 변수에 담는다.
    current = q.popleft()
    for v in vertices[current]:
        if parent[v] == 0:
            parent[v] = current
            q.append(v)
            
print('\n'.join(map(str, parent[2:])))

