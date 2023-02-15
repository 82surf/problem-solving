import math
import sys
sys.stdin = open('input.txt')

n = int(input())
stores = list(map(int, input().split()))
leader, member = map(int, input().split())

answer = len(stores)
for i in range(len(stores)):
    stores[i] -= leader
    if stores[i] > 0:
        answer += math.ceil(stores[i] / member)
print(answer)
