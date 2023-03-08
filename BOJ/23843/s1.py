from heapq import heapify, heappush, heappop
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
batteries = sorted(list(map(int, input().split())))
start, end = N - M, N

power_socket = batteries[start:end]

total = 0
while power_socket:
    # 충전
    min_t = power_socket[0]
    total += min_t
    for i in range(len(power_socket)):
        power_socket[i] -= min_t

    # 충전 완료된 전자기기 제거
    while power_socket and power_socket[0] == 0:
        heappop(power_socket)

    # 빈 콘센트 수만큼 전자기기 꽂기
    empty_cnt = M - len(power_socket)
    while empty_cnt and start > 0:
        start -= 1
        next_battery = batteries[start]
        heappush(power_socket, next_battery)
        empty_cnt -= 1

print(total)
