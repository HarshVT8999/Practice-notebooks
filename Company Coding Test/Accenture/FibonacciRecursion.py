

# def Fibonacci(n):
#     curr = 1
#     prev = 1
#     if n == 1 or n == 2:
#         print(1)
#     for i in range(n-2):
#         next = curr + prev
#         prev = curr
#         curr = next

#     print(next)


# Fibonacci(8)

# Finding the nth Fibonacci number using recursion

def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


x = fib(8)

print(x)
