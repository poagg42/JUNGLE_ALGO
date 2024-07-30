"""
팩토리얼 0의 개수
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	87194	40958	34385	46.611%
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

예제 입력 1 
10
예제 출력 1 
2
예제 입력 2 
3
예제 출력 2 
0

"""

# 팩토리얼을 구한다.

# 구한 값을 쪼개서 배열에 넣는다.

# 0이 아닐 때까지 반복, 수 count



# 내 풀이 - 메모리 초과 뜸

# import sys 
# sys.setrecursionlimit(10**7)

# input = sys.stdin.readline

# N = int(input())
# answer = []
# count = 0


# def factorial(N):
#     global answer
#     if N == 1:
#         return 1
#     return N * factorial(N - 1)

# answer = list(str(factorial(N)))

# answer = answer[::-1]

# for i in answer:
#     if i != '0':
#         break
#     count += 1


# print(count)


# Claude's 풀이

import sys 

input = sys.stdin.readline 

N = int(input())
count = 0

while N >= 5:
    count += N // 5
    N //= 5

print(count)