import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

min_time = 10 ** 10
height = None
for target_height in range(257):
    fill_cnt = 0
    dig_cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] > target_height:
                dig_cnt += ground[i][j] - target_height
            else:
                fill_cnt += target_height - ground[i][j]

    if fill_cnt >  dig_cnt + B:
        continue

    time = fill_cnt + dig_cnt * 2
    if min_time >= time:
        min_time = time
        height = target_height

print(min_time, height)