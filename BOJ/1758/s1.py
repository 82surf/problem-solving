import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tips = sorted([int(input()) for _ in range(N)], reverse=True)
answer = 0
for i, tip in enumerate(tips):
    answer += tip - i if tip >= i else 0
print(answer)