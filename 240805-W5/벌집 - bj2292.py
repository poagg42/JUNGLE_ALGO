import sys 

input = sys.stdin.readline 

N = int(input())

if N == 1:
    print(1)
else:
    room_count = 1
    rooms = 1
    while rooms < N:
        rooms += 6 * room_count
        room_count += 1
    print(room_count)


    