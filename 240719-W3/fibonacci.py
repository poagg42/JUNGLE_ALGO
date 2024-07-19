# Top-Down 방식

import sys 

input = sys.stdin.readline

N = int(input())

def fibonacci(n):
    # 메모이제이션
    # 피보나치 수열을 저장할 배열
    # 이전에 계산한 값 저장 
    # 중복 계산을 피하기 위함
    
    dp = [0] * (N + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i-1] + dp[i-2]


    return dp[n]


print(fibonacci(N))

