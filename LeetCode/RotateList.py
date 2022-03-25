def rotatelist(arr, k):
    for i in range(k):
        first = arr.pop()
        arr.insert(0, first)
    print(arr)


rotatelist([1, 2, 3], 2)
