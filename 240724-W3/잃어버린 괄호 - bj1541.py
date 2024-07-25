import sys 

input = sys.stdin.readline

N = str(input())
M = N.split('-')

answer = 0

x = sum(map(int, (M[0].split('+'))))

if N[0] == '-':
    answer -= x
else:
    answer += x 

for x in M[1:]:
    x = sum(map(int, (x.split('+'))))
    answer -= x 

print(answer)



