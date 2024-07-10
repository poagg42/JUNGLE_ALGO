#    원판갯수, 시작기둥, 중간기둥, 목표기둥
def hanoi(n, start, mid, end):

    # 기저 조건
    if n == 1:
        print(start, end)
        return
        

    # 재귀 조건
    hanoi(n-1, start, end, mid)
    hanoi(1, start, mid, end)
    hanoi(n-1, mid, start, end)


N = int(input())

# N개의 원판이 모두 이동하는 최소 경우의 수
print(2 ** N - 1)

hanoi(N, 1, 2, 3)



    