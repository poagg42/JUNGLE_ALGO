
# 재귀

N = int(input())

def fibonacci(N):
    if N <= 1:
        return N 
    else:
        return fibonacci(N-1) + fibonacci(N-2)
        
print(fibonacci(N))     

# for문 

N = int(input())

def fibonacci(N):
    a, b = 0, 1
    
    for _ in range(1, N + 1):
        a = b
        b = a+b 
    if N <= 1:
        print(N)
    print(b)

fibonacci(N)