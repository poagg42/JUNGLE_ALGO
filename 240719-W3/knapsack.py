# 배낭 문제(Knapsack Problem) -> Bottom-Up

# 주어진 가방의 용량에 최대한 가치가 높은 물건을 넣는 문제 

# 각 물건은 가치와 무게를 가지고 있다.

# bottom-Up 

# 반복문을 이용하여 반복적으로 부분 문제들을 해결하고, 결과를 배열 등에 저장합니다.


import sys 
import math

input = sys.stdin.readline

def knapsack(weights, values, capacity):
    N = len(weights)

    dp = [0] * (N + 1)
    for i in range(0, N + 1):
        dp[i] = [0] * (capacity + 1)

    
    for i in range(1, N + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    return dp[N][capacity]            

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 7

print(knapsack(weights, values, capacity))

# DP 장단점

# 중복 계산을 줄일 수 있습니다.
# 효율적인 시간 복잡도를 가질 수 있습니다.

# 메모리 사용량이 큽니다.

