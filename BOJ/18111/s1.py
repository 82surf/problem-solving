# 오답

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

# 최빈값 탐색
height_dic = {}
for i in range(N):
    for j in range(M):
        if ground[i][j] in height_dic:
            height_dic[ground[i][j]] += 1
        else:
            height_dic[ground[i][j]] = 1

target_height = 0
max_cnt = 0
for height, cnt in height_dic.items():
    if max_cnt < cnt:
        max_cnt = cnt
        target_height = height

# 메워야하는 블록 개수 확인
while True:
    fill_cnt = 0
    cut_cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] < target_height:
                fill_cnt += target_height - ground[i][j]
            elif ground[i][j] > target_height:
                cut_cnt += ground[i][j] > target_height

    if fill_cnt > cut_cnt + B:
        target_height -= 1
    else:
        print(fill_cnt * 1 + cut_cnt * 2, target_height)
        break
