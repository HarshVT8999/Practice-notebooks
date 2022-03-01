# DetectDuplicate

def DetectDuplicate(list):
    hashtable = {}
    flag = 0
    for i, element in enumerate(list):

        if(element in hashtable):
            flag = 1
        hashtable[element] = i

    if flag:
        print("True")
    else:
        print("False")


DetectDuplicate([1, 2, 3, 4])
