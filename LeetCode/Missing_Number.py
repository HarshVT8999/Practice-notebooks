# Missing Number using hash graph

def Missing_Number(list):
    hash = {}
    flag = 0
    for i, element in enumerate(list):
        hash[element] = i

    for i in range(len(list)+1):
        if i not in hash:
            print(i)


# Missing_Number([1, 0, 3])

# Missing number using 0(n)

def Missing_Num(list):
    sum = len(list)
    for i in range(len(list)):
        sum += (i - list[i])
    print(sum)


Missing_Num([1, 0, 3])
