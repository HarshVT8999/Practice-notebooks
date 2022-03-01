def TwoSum(list, target):
    hashtable = {}
    for i, element in enumerate(list):
        rem = target - element
        if(rem in hashtable):
            print([i, hashtable[rem]])
        hashtable[element] = i


TwoSum([1, 2, 3, 4], 4)
