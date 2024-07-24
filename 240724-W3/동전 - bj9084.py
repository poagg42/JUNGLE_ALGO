import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input().strip())
    coins = list(map(int, input().split()))
    K = int(input().strip())

    DP_table = [0]*(K+1)
    DP_table[0] = 1

    for j in range(len(coins)):
        c = coins[j]
        for k in range(c, K+1):
            DP_table[k] += DP_table[k-c]

    print(DP_table[K])

