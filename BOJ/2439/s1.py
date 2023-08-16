N = int(input())
for n in range(1, N + 1):
    space = ' ' * (N - n)
    star = '*' * n
    print(space + star)