def maxSubArray(arr):
    maxSub = arr[0]
    cursum = 0

    for n in arr:
        if cursum < 0:
            cursum = 0
        cursum += n
        maxSub = max(maxSub, cursum)
    print(maxSub)


maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
