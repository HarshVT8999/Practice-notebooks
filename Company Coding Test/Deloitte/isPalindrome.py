def isPalindrome(A):
    y = 0
    n = A
    while n > 0:
        y = y*10 + n % 10
        n = n//10
    print(y)
    if y == A:
        print(1)
    else:
        print(0)


isPalindrome(2147447412)
