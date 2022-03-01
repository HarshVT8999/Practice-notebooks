

# Method 1 (Not using O(n) time complexity)
def prod(list):
    prod = 1
    # list = [1,2,3,4] pre = [1,2,6,24] post = [24,24,12,4]
    for i in range(len(list)):
        prod *= list[i]
    for i in range(len(list)):
        list[i] = prod/list[i]
    print(list)

# prod([1,2,3,4])

# Method 2 (Using O(n) time complexity)


def prod2(list):
    arr = [1]*(len(list))
    pre = 1
    for i in range(len(list)):
        arr[i] = pre
        pre *= list[i]
        print(arr)
    post = 1
    for i in range(len(list)-1, -1, -1):
        arr[i] *= post
        post *= list[i]
        print(arr)
    print(arr)


prod2([1, 2, 3, 4])
