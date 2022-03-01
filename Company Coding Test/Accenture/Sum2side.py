def solve(A, B):
    SumA, SumB = sum(A[:B]), 0
    maxSum = SumA
    i, j = B-1, len(A)-1
    while i > -1:
        SumA -= A[i]
        SumB += A[j]
        maxSum = max(maxSum, SumA+SumB)
        i -= 1
        j -= 1
    print(maxSum)


solve([1, 2, 3, 4, 5], 3)
