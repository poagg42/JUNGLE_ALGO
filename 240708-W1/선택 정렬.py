a = [1,4,2,5,3]

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min = i 
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j 
        a[i], a[min] = a[min], a[i]
    return a

selection_sort(a)

for i in a:
    print(i)

