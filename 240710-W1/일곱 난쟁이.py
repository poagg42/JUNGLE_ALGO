height = []

for _ in range(9):
    height.append(int(input()))

total_sum = sum(height)
found = False

for i in range(8):
    for j in range(i + 1, 9):
        if total_sum - (height[i] + height[j]) == 100:
            height1, height2 = height[i], height[j]
            height.remove(height1)
            height.remove(height2)
            found = True 
            break 
    if found:
        break

height.sort()

for i in height:
    print(i)