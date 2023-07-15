import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
dic = {0: 1}
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + A[i]

    val = prefix_sum[i+1] - K
    if val in dic:
        answer += dic[val]

    if prefix_sum[i+1] not in dic:
        dic[prefix_sum[i+1]] = 1
    else:
        dic[prefix_sum[i + 1]] += 1

print(answer)