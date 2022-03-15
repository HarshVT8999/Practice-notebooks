# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

cur = 1
prev = 1
for i in range(5):
    temp = cur
    cur = cur + prev
    prev = temp
    print(prev)
