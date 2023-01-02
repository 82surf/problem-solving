import sys
sys.stdin = open('input.txt')

max_n, max_i = 0, 0
for i in range(1, 10):
    n = int(input())
    if max_n < n:
        max_n = n
        max_i = i
print(max_n)
print(max_i)