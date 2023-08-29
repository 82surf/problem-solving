import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = dict.fromkeys(list(input()))

answer = abs(N - 100)

for i in range(1000001):
    num = str(i)
    for idx, char in enumerate(num):
        if char in broken:
            break
        elif idx == len(num) - 1:
            val = len(num) + abs(i - N)
            answer = min(answer, val)

print(answer)
