def minStepToCoverGrid(A, B):   # A = x coordinate ; B = y coordinate
    steps = 0
    for i in range(len(A)-1):
        if abs(A[i]-A[i+1]) <= abs(B[i]-B[i+1]):
            steps += abs(B[i]-B[i+1])
        else:
            steps += abs(A[i]-A[i+1])
    print(steps)

# A : [ -7, -13 ]
# B : [ 1, -5 ]


minStepToCoverGrid([-7, -13], [1, -5])
