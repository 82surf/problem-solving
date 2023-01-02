import sys
sys.stdin = open('input.txt')

n = 1
for _ in range(3):
    n *= int(input())

ans = [0 for _ in range(10)]
for i in str(n):
    ans[int(i)] += 1

for i in ans:
    print(i)