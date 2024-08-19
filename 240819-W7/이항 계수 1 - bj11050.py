# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 구하는 프로그램

# nCk = n! / (n - k)! k!

import sys 

input = sys.stdin.readline 

N, K = map(int, input().split())

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


nCk = factorial(N) / (factorial(N - K) * factorial(K))

print(int(nCk))