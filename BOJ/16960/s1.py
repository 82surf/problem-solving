import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
lamp_connect_count = dict.fromkeys(range(1, M + 1), 0)
switch_connect_info = [{} for _ in range(N + 1)]

for switch in range(1, N + 1):
    connect_info = list(map(int, input().split()))
    for j in range(1, len(connect_info)):
        lamp = connect_info[j]
        switch_connect_info[switch][lamp] = True
        lamp_connect_count[lamp] += 1


def solution():
    for i in range(1, len(switch_connect_info)):
        connect_info = switch_connect_info[i]
        for lamp in connect_info:
            if lamp_connect_count[lamp] == 1:
                break
        else:
            return 1
    return 0

print(solution())
