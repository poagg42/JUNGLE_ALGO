"""
큐 2
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (하단 참고)	512 MB	103916	33655	27239	32.581%
문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1 
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
예제 출력 1 
1
2
2
0
1
2
-1
0
1
-1
0
3

"""

import sys 
from collections import deque

input = sys.stdin.readline


N = int(input())
deq = deque()

for i in range(N):
    inputValue = input().split()

    # push

    if inputValue[0] == 'push':
        deq.append(inputValue[1])

    # pop 
    elif inputValue[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()

    # size 
    elif inputValue[0] == 'size':
        print(len(deq))
    
    # empty
    elif inputValue[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    # front
    elif inputValue[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    
    # back
    elif inputValue[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])





# test

# a = []

# a.append(1)
# a.append(4)
# a.append(5)
# a.append(2)
# a.append(3)
# a.append(6)

# print(a)

# a.pop(0)

# print(a)

# a.pop(0)

# print(a)

# a.pop(0)

# print(a)

# a.pop(0)

# print(a)

# a.pop(0)

# print(a)

# a.pop(0)

# print(a)
