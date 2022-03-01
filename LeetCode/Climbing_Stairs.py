cur = 1
prev = 1
for i in range(5):
    temp = cur
    cur = cur + prev
    prev = temp
    print(prev)
