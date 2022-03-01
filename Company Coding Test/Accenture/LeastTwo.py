
def Operation(c, a, b):
    switcher = {
        1: a+b,
        2: a-b,
        3: a*b,
        4: a//b
    }

    print(switcher.get(c))


Operation(2, 16, 20)
