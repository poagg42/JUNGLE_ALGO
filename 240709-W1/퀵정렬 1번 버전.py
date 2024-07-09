import sys 
input = sys.stdin.readline

N = int(input())
a = []

for _ in range(N):
    a.append(int(input()))

def qsort(a, left, right):
    pl = left 
    pr = right
    pivot = a[(left + right) // 2]

    # pl이 pr보다 작을 때 반복 유지

    while pl <= pr:

        # pl값이 pivot보다 작을 때 반복 유지

        while a[pl] < pivot:
            pl += 1

        # pr값이 pivot보다 클 때 반복 유지
        while a[pr] > pivot:
            pr -= 1

        # pl값과 pr값 바꿈    
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(a, left, pr)
    if pl < right:
        qsort(a, pl, right)


def quicksort(a):
    qsort(a, 0, len(a)-1)
    


quicksort(a)

for i in a:
    print(i)
