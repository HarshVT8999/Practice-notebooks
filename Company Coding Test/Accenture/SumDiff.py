def sumDiff(t, n):
    sum1 = 0
    sum2 = 0
    for i in range(1, t+1):
        if i % n == 0:
            sum1 += i
        else:
            sum2 += i
    print(abs(sum2-sum1))


sumDiff(10, 3)
