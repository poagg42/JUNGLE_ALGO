"""
최대공약수와 최소공배수
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	118771	68594	55955	57.771%
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1 
24 18
예제 출력 1 
6
72

"""

import sys 

# 내 풀이

# input = sys.stdin.readline

# valueList = list(map(int, input().split()))
# GCD = [] # 최대 공약수
# LCM = [] # 최소 공배수

# a = valueList[0]
# b = valueList[1]

# # 최대 공약수
# def gcd_make(list, a, b):
#     for i in range(1, min(a, b)):
#         if a & i == 0 and b % i == 0:
#             list.append(i)


# gcd_make(GCD, a, b)

# print(GCD[-1])

# x = a 
# y = b
# storedValue = []

# def lcm_make():
#     gcd_make(storedValue, x, y)
    
#     first = x // storedValue[-1]
#     second = y // storedValue[-1]

#     print(storedValue[-1] * first * second)

# lcm_make()


def gcd(a, b):
    while b:
        a, b = b, a % b 
    return a 

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, sys.stdin.readline().split())

print(gcd(a, b))
print(lcm(a, b))