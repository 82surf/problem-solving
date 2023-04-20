import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
secret = ''.join(list(input().split()))
button = ''.join(list(input().split()))

print('secret') if secret in button else print('normal')