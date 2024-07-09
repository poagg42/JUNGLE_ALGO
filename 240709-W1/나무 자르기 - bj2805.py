"""
나무 자르기 다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	207125	61320	38063	26.281%
문제
상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

예제 입력 1 
4 7
20 15 10 17
예제 출력 1 
15
예제 입력 2 
5 20
4 42 40 26 46
예제 출력 2 
36
"""

# sudo code

# 다 더하고 N으로 나눈다.(평균을 구함)
# 모든 값을 순회하고 i에서 average를 뺀다
# 음수면 버림
# 이것들을 더한 값이 M이상일 때 반복 멈춤
# average에 1씩 더하면서 반복

# 내 풀이

import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
treeList = list(map(int, input().split()))
average 
count = 0
difference = 0
for i in treeList:
    average += i

# 평균을 구함

average = average // N 


# difference가 M보다 작을 때 반복
while True:
    difference = 0

    for i, x in enumerate(treeList):
        if treeList[i] - average < 0:
            continue
        difference += treeList[i] - average
    
    # 차이가 M과 같을 때 탈출
    if difference == M:
        break

    average += 1

print(average)

# 인터넷 풀이

# import sys 
# input = sys.stdin.readline 

# # 입력
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))

# start, end = 1, max(lst) # 초기 시작과 끝 값 설정

# while start <= end:
#     sum = 0
#     mid = (start + end) // 2 # 중간값 설정

#     for l in lst:
#         if l > mid:
#             sum += l - mid # 중간값을 기준으로 잘랐을 때 가져갈 수 있는 나무 길이 합 계산

#     if sum < m: # 가져갈 수 있는 나무 길이 합이 목표보다 작은 경우
#         end = mid - 1
#     else: # 가져갈 수 있는 나무 길이 합이 목표보다 크거나 같은 경우
#         start = mid + 1
        
# print(end)

 


