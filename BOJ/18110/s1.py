import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
ratings = sorted([int(input()) for _ in range(n)])

if n == 0:
    print(0)
else:
    except_n = round(n * 15 / 100 + 0.0000001)
    print(round(sum(ratings[except_n:n - except_n]) / (n - except_n * 2) + 0.0000001))