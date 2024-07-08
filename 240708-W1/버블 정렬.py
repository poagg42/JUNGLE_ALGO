a = [1,3,5,2,4]

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, - 1):
            if a[j - 1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


bubble_sort(a)

for i in a:
    print(i)