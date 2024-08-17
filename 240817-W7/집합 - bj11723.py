"""
집합 언어 제한
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1.5 초	4 MB (하단 참고)	115770	35337	26110	29.572%
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.

예제 입력 1 
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
예제 출력 1 
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0

"""

# import sys 

# input = sys.stdin.readline

# M = int(input())

# valueList = []

# for _ in range(M):
#     # valueList = list(map(int, valueList))

#     command = input().split()
#     if len(command) == 1:
#         operation = command[0]
#         value = None
#     else:
#         operation, value = command
    
#     # add x : S에 x를 추가한다.
#     if operation == "add":
#         valueList.append(value)
    
#     # remove x : S에서 x를 제거한다.
#     if operation == "remove":
#         if valueList.count(value):
#             valueList.remove(value)

#     # check x : S에 x가 있으면 1을, 없으면 0을 출력한다.
#     if operation == "check":
#         # print(valueList, 'checkValueList')
#         if valueList.count(value):
#             print(1)
#         else:
#             print(0)

#     # toggle x : S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
#     if operation == "toggle":
#         if valueList.count(value):
#             valueList.remove(value)
#         else:
#             valueList.append(value)       

#     # all : S를 {1, 2, ... , 20} 으로 바꾼다.

#     if operation == "all":
#         newValueList = []

#         for i in range(1, 21):
#             newValueList.append(i)

#         newValueList = list(map(str, newValueList))

#         valueList = newValueList
#         # print(valueList, 'all')

#     # empty : S를 공집합으로 바꾼다.

#     if operation == "empty":
#         valueList = []    
          

import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
