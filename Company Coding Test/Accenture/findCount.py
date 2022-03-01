def findCount(arr, num, diff):
    count = 0
    for i in range(len(arr)):
        dif1 = abs(num-arr[i])
        if dif1 <= diff:
            count += 1

    print(count)


findCount([12, 3, 14, 56, 77, 13], 13, 2)
