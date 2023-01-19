n = int(input())
s_root = int(n ** 0.5)

if s_root ** 2 == n:
    print(s_root)
else:
    while s_root ** 2 < n:
        s_root += 1
    print(s_root)