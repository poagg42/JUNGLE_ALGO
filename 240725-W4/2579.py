import sys 

input = sys.stdin.readline 

N = int(input())
numList = []
answerList = []


for _ in range(N):
    a = int(input())
    numList.append(a)

print(numList, 'init numList')

n = len(numList)

# 마지막 계단 밟기

answerList.append(numList[-1])

# 마지막 계단을 제외하고 연속된 두 계단 비교하기
# 비교해서 answerList에 담기

while True:

    if n == 2:
        break
    
    if numList[n-2] >= numList[n-3]:
        answerList.append(numList[n-2])
    elif numList[n-2] < numList[n-3]:
        answerList.append(numList[n-3])
    
    n -= 1


print(answerList, 'answerList1')

# 연속된 계단들, 중복 제거하기

m = 1

while True:

    if m >= len(answerList) - 1:
        break
    
    if answerList[m] == answerList[m + 1]:
        answerList.pop(m+1)

    m += 1
    
    
print(answerList, 'answerList2')



# 연속된 세 계단이 아닌 값을 추가한다.

# 연속된 세 계단을 어떻게 구분할 것인가?

# 풀이는 여기까지... 못찾겠다.

