def get_decomposition(n):
    nums = list(map(int, list(str(n))))
    return n + sum(nums)


N = int(input())
answer = 1000001
for i in range(N):
    decomposition = get_decomposition(i)
    if decomposition == N and answer > i:
        answer = i
        break
else:
    answer = 0
print(answer)
