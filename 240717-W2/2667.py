"""
단지번호붙이기
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	191438	85954	54675	42.760%
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
"""

import sys 
from collections import deque

input = sys.stdin.readline 

# 지도의 크기 입력받기
N = int(input())
houseList = []
count = 0

# 집 입력받기

for _ in range(N):
    split = []
    house = str(input().rstrip())
    split = list(house)
    houseList.append(split)


# Int로 변환 

houseList = [[int(cell) for cell in row] for row in houseList]

print(houseList)    


# bfs로 돌면서 0을 만나면 count 중지, 1을 만나면 count + 1


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def bfs(x, y):
    global count

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and houseList[nx][ny] == 1:
                count += 1
                queue.append((nx, ny))
                houseList[nx][ny] = houseList[x][y] + 1


    return count 
from collections import deque
def bfs2(graph,start,visited):
    
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        

        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    

# bfs를 이용해 count를 세어봤는데 단지수와 집의 수를 제대로 구하지 못했다.
visited = [False]*len(graph)
print(bfs(0, 0) - 1)

print(bfs(N, 0) - 1)

print(bfs(0, N) - 1)


