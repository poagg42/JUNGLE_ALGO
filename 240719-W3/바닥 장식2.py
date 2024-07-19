# 바닥 장식2

"""
수도 코드

dfs(x, y)

해당 노드 방문 처리 
'-'인 경우 - 오른쪽 노드가 '-'이면 -> dfs(x + 1, y, '-') 오른쪽 노드가 '|'이면 -> return
'|'인 경우 - 아래 노드가 '|'이면 -> dfs(x, y + 1, '|') 아래 노드가 '-'이면 -> return

방문하지 않는 노드이면 반복
return 



"""

# dfs는 탈출 조건 - 다음 노드를 판단하는 로직 - 다음 노드에 가서 수행하는 로직

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

place = []

for _ in range(N):
    place.append(list(input()))

def dfs(row, col):

    # - 일때
    if place[row][col] == "-":
        # 방문처리
        place[row][col] = 1
        # 같은행 확인하기 양옆
        for a in [1, -1]:
            # 같은 나무판자로 만들기
            Y = col + a
            # 가로를 벗어나지 않고 다음 노드가 -라면 다시 재귀
            if (0 < Y < M) and place[row][Y] == "-":
                dfs(row, Y)

    # | 일때
    if place[row][col] == "|":
        # 방문처리
        place[row][col] = 1
        for b in [1, -1]:
            # 같은 나무판자로 만들기
            X = row + b
            # 가로를 벗어나지 않고 다음 노드가 |라면 다시 재귀
            if (0 < X < N) and place[X][col] == "|":
                # dfs 반복
                dfs(X, col)

count = 0 
for i in range(N):
    for j in range(M):
        if place[i][j] == '-' or place[i][j] == '|':
            dfs(i, j)
            count += 1

print(count)