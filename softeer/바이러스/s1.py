# 시간초과

import sys
input = sys.stdin.readline

K, P, N = map(int, input().split())
print(K * P ** N % 1000000007)