import sys 
input = sys.stdin.readline

N = int(input())
a = []
a = [4,2,1,3,5]

for _ in range(N):
    a.append(int(input()))

def quick_sort(a):

    if len(a) <= 1:
        return a 
    
    pivot = a[0]
    tail = a[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side) 

newList = quick_sort(a)

for i in newList:
    print(i)