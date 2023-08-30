import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
dp = [0] * N
if N <= 2:
    print(sum(S))
else:
    dp[0] = S[0]
    dp[1] = S[0] + S[1]
    for i in range(2, N):
        case_1 = dp[i - 3] + S[i - 1] + S[i]
        case_2 = dp[i - 2] + S[i]
        dp[i] = max(case_1, case_2)
    print(dp[-1])
