"""
N-Queen 
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
10 초	128 MB	120364	57923	37515	46.644%
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
"""

import sys 
input = sys.stdin.readline

N = int(input())

# 퀸이 공격을 받는지 확인
def attack(x):
    for i in range(x):
        # 같은 행에 퀸이 있거나 대각선에 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return True 
    return False

def dfs(start):
    global cnt 

    if start == N:
        cnt += 1
    else:
        for i in range(N):
            row[start] = i 
            if not attack(start):
                dfs(start + 1)

row = [0] * N 
cnt = 0
dfs(0)

print(cnt)

