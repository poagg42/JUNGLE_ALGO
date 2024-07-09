a = [5, 7, 1, 4, 6, 2, 3, 9, 8]

def quickTest():
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    print('피벗 이하인 그룹입니다.')
    print(*a[0 : pl]) # a[0] ~ a[pl - 1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl])
        print('피벗 이상인 그룹입니다.')
        print(*a[pr + 1 : n])

