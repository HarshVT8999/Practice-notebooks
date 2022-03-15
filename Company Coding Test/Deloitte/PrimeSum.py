# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
import math


def isPrime(A):
    if A == 1:
        return 0
    if A == 2 or A == 3:
        return 1
    if A % 2 == 0 or A % 3 == 0:
        return 0
    for i in range(5, int(math.sqrt(A))+1, 6):
        if A % i == 0 or A % (i+2) == 0:
            return 0
    return 1


def primesum(A):
    if A == 4:
        return [2, 2]
    elif A == 6:
        return [3, 3]
    b = A//2
    for x in range(3, b, 2):
        c = A-x
        if (isPrime(x) == 1 and isPrime(c) == 1):
            print([x, c])


primesum(10)
