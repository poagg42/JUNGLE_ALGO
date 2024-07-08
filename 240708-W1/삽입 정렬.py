N = int(input())
a = []

for _ in range(N):
    value = int(input())
    a.append(value)

def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        j = i 
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
         
    return a   

insertion_sort(a)

for i in a:
    print(i)




