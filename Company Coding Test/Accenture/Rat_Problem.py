r = 7
unit = 2
n = 8
arr = [2, 8, 3, 5, 7, 4, 1, 2]

sum = 0
food = r*unit
for i in range(n):
    sum += arr[i]
    if sum > food:
        print(i+1)
        break
