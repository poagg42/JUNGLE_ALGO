# 잘못된 풀이, 점화식이 아니라 다른 방식으로 풀어야 한다.

N = int(input())
count = 2

def N_Queen(N, count):
    # 점화식: 2 * f(n-1) + 4

    # 기저 조건
    if N == 1:
        print(1)
    elif N == 2:
        print(0)
    elif N == 3:
        print(0)    
    elif N == 4:
        print(count)

    # 재귀 조건
    else:
        count *= 2
        count += 4
        N_Queen(N-1, count)

if(1 <= N < 15):
    N_Queen(N, count)
