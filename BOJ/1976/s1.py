import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


for city_1 in range(1, N + 1):
    connection_info = list(map(int, input().split()))
    for idx, connected in enumerate(connection_info):
        city_2 = idx + 1
        if connected and city_1 != city_2:
            union(city_1, city_2)

plan = list(map(int, input().split()))

answer = 'YES'
for i in range(len(plan) - 1):
    city_1, city_2 = plan[i], plan[i + 1]
    if find(city_1) != find(city_2):
        answer = 'NO'
        break

print(answer)
