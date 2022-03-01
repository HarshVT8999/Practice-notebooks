def Sum(A, B):
    m = len(A)
    n = len(B)
    res = [0] * max(m, n)
    max_len = 0
    # make sure that the least number is assigned to A
    if m < n:
        A = [0] * abs(m-n) + A
        max_len = n
    else:
        B = [0] * abs(m-n) + B
        max_len = m

    carry = 0

    for i in reversed(range(max_len)):
        curr_sum = A[i] + B[i] + carry
        if curr_sum > 9:
            res[i] = curr_sum % 10
            carry = curr_sum // 10
        else:
            res[i] = curr_sum
            carry = 0

    if carry != 0:
        print([carry] + res)
    else:
        print(res)


Sum([1, 1, 1, 2], [9, 9, 2])
