S = input()
for i in range(97, 123):
    c = chr(i)
    if c in S:
        print(S.index(c), end=" ")
    else:
        print('-1', end=" ")
