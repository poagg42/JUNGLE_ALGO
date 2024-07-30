# DP 피보나치 상향식

def fib_bottom_up(n):
    if n<=1:
        return n

    # 초기 피보나치
    fib_0 = 0
    fib_1 = 1

    for i in range(2, n + 1):
        next_fib = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = next_fib
    
    return fib_1


# DP 피보나치 하향식

memoization = [0] * 100

def fib_top_down(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있으면 그대로 반환
    if memoization[x] != 0:
        return memoization[x]
    # 계산한 적 없으면 점화식에 따라 피보나치 결과 반환
    memoization[x] = fib_top_down(x - 1) + fib_top_down(x - 2)
    return memoization[x]


