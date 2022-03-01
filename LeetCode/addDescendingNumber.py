# recursion function for adding odd numbers in the reverse order
def addDescendingNumber(a):
    newNumber = a
    sum = newNumber
    newNumber -= 1
    sum += newNumber

    if newNumber != 0:
        sum += addDescendingNumber(newNumber-1)

    print(sum)
    return sum


addDescendingNumber(5)
