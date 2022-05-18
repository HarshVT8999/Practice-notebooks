def TwoSum(list, target):
    hashtable = {}
    for i, element in enumerate(list):
        rem = target - element
        if(rem in hashtable):
            print([hashtable[rem], i])
        hashtable[element] = i


TwoSum([1, 2, 3, 4], 4)
