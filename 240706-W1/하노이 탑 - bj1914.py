"""
하노이 탑
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
6 초	128 MB	37637	8066	6187	23.432%
문제
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.



입력
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄에 옮긴 횟수 K를 출력한다.

N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.

예제 입력 1 
3
예제 출력 1 
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3

"""

# 내가 생각했던 풀이

# N = int(input())

# def makeTop(N):
#     for i in range(1, N+1):
#         firstTop.append(i)
#     firstTop = firstTop[::-1]
        





# print(firstTop)

# firstTop.pop()

# print(firstTop)

# # 횟수
# print(2 ** N - 1)

# 이동로직 구현
# while(len(firstTop) != 0 and len(secondTop) != 0):
#     if len(firstTop) % 2 == 1:
#         thirdTop.append(firstTop.pop())
#         print(f'1 3')
#         secondTop.append(firstTop.pop())
#         print(f'1 2')
#         secondTop.append(thirdTop.pop())
#         print(f'3 2')
#         if len(firstTop) == 0:



# def hanoi(N):
#     # 기저조건
#     if len(top) == 0:
#         return
#     # 홀수면서 firstTop인 경우
#     if len(top) % 2 == 1 and top == firstTop:
#         thirdTop.append(top.pop())
#     # 홀수면서 secondTop인 경우
#     elif len(top) % 2 == 1 and top == secondTop:
#         thirdTop.append(top.pop())
#     # 홀수면서 thirdTop인 경우
#     elif len(top) % 2 == 1 and top == thirdTop:
#         secondTop.append(top.pop())
    
#     return hanoi()
        

# 인터넷에서 가져온 풀이

def hanoi(n, from_p, mid_p, to_p):

    if n == 1:
        print(from_p, to_p, sep = " ")

    else:

        hanoi(n-1, from_p, to_p, mid_p)

        hanoi(1, from_p, mid_p, to_p)

        hanoi(n-1, mid_p, from_p, to_p)

a = int(input())

print(2**a-1)

if(a<=20):
    hanoi(a, 1, 2, 3)

