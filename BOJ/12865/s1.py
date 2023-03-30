import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
w = [0] * (N + 1)
v = [0] * (N + 1)
idx = 0
for _ in range(N):
    idx += 1
    W, V = map(int, input().split())
    w[idx] = W
    v[idx] = V

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    curr_w, curr_v = w[i], v[i]
    for j in range(1, K + 1):
        # 첫번째 물건 탐색하며 초깃값 넣기
        if i == 1 and curr_w <= j:
            dp[i][j] = curr_v
        # 현재 가방 무게에 현재 물건을 넣을 수 있다면
        elif j >= curr_w:
            val1 = dp[i - 1][j]
            val2 = dp[i - 1][j - curr_w] + curr_v
            dp[i][j] = val1 if val1 > val2 else val2
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])

