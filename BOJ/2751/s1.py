import sys
sys.stdin = open('input.txt')
N = int(input())
arr = sorted(list(map(int, sys.stdin.readlines())))
for n in arr:
    print(n)