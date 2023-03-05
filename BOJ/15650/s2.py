def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for c in combinations(arr[i+1:], r-1):
                yield [arr[i]] + c


N, M = map(int, input().split())
for c in combinations(range(1, N+1), M):
    print(*c)
