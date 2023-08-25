import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

people_didnt_listen = {}

for _ in range(N):
    people_didnt_listen[input().rstrip()] = 1

answer = []
for _ in range(M):
    name = input().rstrip()
    if name in people_didnt_listen:
        answer.append(name)
answer.sort()

print(len(answer))
for name in answer:
    print(name)
