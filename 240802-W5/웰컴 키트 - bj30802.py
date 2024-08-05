# 첫 줄에 참가자 N

# 둘째 줄에 티셔츠 사이즈 별 신청자의 수 S, M, L, XL, XXL, XXXL이 공백으로 구분되어 주어집니다.

# 셋째 줄에 정수 티셔츠와 펜의 묶음 수를 의미하는 T, P

# 처음에 틀린 이유 : 여러 예외사항을 고려하자.

import sys 

input = sys.stdin.readline

N = int(input())

tList = list(map(int, input().split()))
T, P = map(int, input().split())

count = 0

for i in tList:
    if i // T == 0 | i == T:
        count += 1
    elif i % T == 0:
        count += i // T
    else:
        count += (i // T) + 1

print(count)
print(N // P, N % P)