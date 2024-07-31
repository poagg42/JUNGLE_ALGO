"""
좌표 정렬하기
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	149599	72085	56113	48.201%
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

예제 입력 1 
5
3 4
1 1
1 -1
2 2
3 3
예제 출력 1 
1 -1
1 1
2 2
3 3
3 4

"""

# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 내 풀이

# import sys 

# input = sys.stdin.readline

# N = int(input())
# xList = []
# yList = []

# for _ in range(N):
#     x, y = map(int, input().split())
#     xList.append(x)
#     yList.append(y)

# xList.sort()
# yList.sort()

# lenX = len(xList)

# xList.extend(yList)

# for i in range(lenX):
#     print(xList[i], xList[i+lenX])


# 인터넷 풀이

import sys 

input = sys.stdin.readline

N = int(input())

li = []

for i in range(N):
    [a, b] = map(int, input().split())
    li.append([a, b])

li.sort()
for i in li:
    print(i[0], i[1])