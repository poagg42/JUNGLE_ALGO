"""
분해합 다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	192 MB	163293	75615	59477	45.404%
문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

예제 입력 1 
216
예제 출력 1 
198
"""

# 어떤 자연수 N이 있을 때 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합.

# 245의 분해합은 245 + 2 + 4 + 5
# 245는 256의 생성자가 된다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램

import sys

input = sys.stdin.readline

N = int(input())

numList = []
answerList = []

# 분해합 구하는 식

answer = 0


def decomSum(x):
    global answer
    answer = 0
    strX = str(x)

    for i in range(len(strX)):
        answer += int(strX[i])
    answer += x

# 돌리면서 decomSum이 216이 되는 수를 찾아야 한다.

for i in range(1, N):
    numList.append(i)

# 이 numList를 함수에 넣자.

for i in range(len(numList)):
    decomSum(numList[i])
    if answer == N:
        answerList.append(numList[i])

if len(answerList) != 0:
    print(answerList[0])
else:
    print(0)



