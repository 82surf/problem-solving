# dp


def solution():
    dp = [0] * 50001
    n = int(input())

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1

        j = 1
        while j ** 2 <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    print(dp[n])


solution()
