import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
dp = [0] * 101
for idx, n in enumerate([1, 1, 1, 2, 2]):
    dp[idx + 1] = n
for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for _ in range(T):
    print(dp[int(input())])