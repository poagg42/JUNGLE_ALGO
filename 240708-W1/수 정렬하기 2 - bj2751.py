import sys 
import random 
# input = sys.stdin.readline

# N = int(input())
# a = []

# for _ in range(N):
#     value = int(input())
#     a.append(value)

# 선택 정렬 

# def selection_sort(a):
#     n = len(a)
#     for i in range(n - 1):
#         min = i
#         for j in range(i+1, n):
#             if a[j] < a[min]:
#                 min = j 
#         a[i], a[min] = a[min], a[i]
#     return a

# selection_sort(a)

# 쉘 정렬

# def shell_sort(a):
#     n = len(a)
#     h = n // 2
#     while h > 0:
#         for i in range(h, n):
#             j = i - h 
#             tmp = a[i]
#             while j >= 0 and a[j] > tmp:
#                 a[j + h] = a[j]
#                 j -= h
#             a[j + h] = tmp 
#         h //= 2
#         return a

# shell_sort(a)    

# for i in a:
#     print(i)

# 퀵 정렬

def qsort(a, left, right):
    if left >= right:
        return

    pl = left
    pr = right
    pivot_index = random.randint(left, right)
    pivot = a[pivot_index]
    
    a[pivot_index], a[(left + right) // 2] = a[(left + right) // 2], a[pivot_index]
    
    while pl <= pr:
        while a[pl] < pivot: pl += 1
        while a[pr] > pivot: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a):
    qsort(a, 0, len(a) - 1)

def main():
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    
    quick_sort(a)

    for i in a:
        print(i)

if __name__ == "__main__":
    main()