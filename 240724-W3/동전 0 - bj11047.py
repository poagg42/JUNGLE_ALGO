import sys

input = sys.stdin.readline

N, K = map(int, input().split())

moneyList = []
newMoneyList = []
count = 0

for _ in range(N):
    a = int(input())
    moneyList.append(a)

for i in moneyList:
    if i <= K:
        newMoneyList.append(i)

while K > 0:
    if K < newMoneyList[-1]:
        newMoneyList.pop()

    count += int(K / newMoneyList[-1])
    newNum = K % newMoneyList[-1]

    if newNum == 0:
        break

    K = newNum
    newMoneyList.pop()

print(count)








        

        

