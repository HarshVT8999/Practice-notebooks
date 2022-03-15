# Given an integer n, return true if it is a power of two. Otherwise, return false
import math


def isPowerOfTwo(n):
    if(n <= 0):
        return False
    res = math.log(n, 2)
    print(res)
    if int(res) == round(res, 9):
        print("True")
    else:
        print("False")


isPowerOfTwo(16)
