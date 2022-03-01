from itertools import count


def sort012(arr, n):
    # code here
    temp = [0]*3
    output = [0]*n
    for num in arr:
        temp[num] += 1
    for i in range(1, 3):
        temp[i] += temp[i-1]
    for i in range(n):
        output[temp[arr[i]]-1] = arr[i]
        temp[arr[i]] -= 1
    for i in range(n):
        arr[i] = output[i]
    print(arr)


sort012([0, 2, 1, 2, 0], 5)
