def factorial(n, k):
    if k <= 1:
        return n
    return factorial(n * k, k - 1)


print(factorial(1, int(input())))
