# input.txt에 있는 tc에서 틀림
# 정답: 10 | 아래 코드 출력: -1

from copy import deepcopy
import sys
sys.stdin = open('input.txt')


def solution(k, box, red=None, blue=None, dir_idx=None):
    global answer

    # 백트래킹
    if k >= answer:
        return

    # red, blue 중 하나라도 없으면 탐색해서 좌표 설정
    if not red or not blue:
        for i in range(N):
            for j in range(M):
                if box[i][j] == 'R':
                    red = [i, j]
                elif box[i][j] == 'B':
                    blue = [i, j]

    for idx, dir in enumerate(dirs):
        if idx == dir_idx:
            continue
        next_box = deepcopy(box)
        next_red, next_blue = red[:], blue[:]
        is_red_in, is_blue_in = False, False

        # red 옮기기
        def move_red():
            nonlocal next_red, is_red_in
            next_box[next_red[0]][next_red[1]] = '.'
            while 0 <= next_red[0] + dir[0] < N and 0 <= next_red[1] + dir[1] < M:
                if next_box[next_red[0] + dir[0]][next_red[1] + dir[1]] == '#' or next_box[next_red[0] + dir[0]][next_red[1] + dir[1]] == 'B':
                    break
                elif next_box[next_red[0] + dir[0]][next_red[1] + dir[1]] == 'O':
                    is_red_in = True
                    break
                next_red = [next_red[0] + dir[0], next_red[1] + dir[1]]
            if not is_red_in:
                next_box[next_red[0]][next_red[1]] = 'R'

        # blue 옮기기
        def move_blue():
            nonlocal next_blue, is_blue_in
            next_box[next_blue[0]][next_blue[1]] = '.'
            while 0 <= next_blue[0] + dir[0] < N and 0 <= next_blue[1] + dir[1] < M:
                if next_box[next_blue[0] + dir[0]][next_blue[1] + dir[1]] == '#' or next_box[next_blue[0] + dir[0]][next_blue[1] + dir[1]] == 'R':
                    break
                elif next_box[next_blue[0] + dir[0]][next_blue[1] + dir[1]] == 'O':
                    is_blue_in = True
                    break
                next_blue = [next_blue[0] + dir[0], next_blue[1] + dir[1]]
            if not is_blue_in:
                next_box[next_blue[0]][next_blue[1]] = 'B'

        diff = [next_red[0] - next_blue[0], next_red[1] - next_blue[1]]
        if (dir == (0, 1) and diff[1] > 0) or (dir == (1, 0) and diff[0] > 0) or (dir == (-1, 0) and diff[0] < 0) or (dir == (0, -1) and diff[1] < 0):
            move_red()
            move_blue()
        else:
            move_blue()
            move_red()

        # 처리된 박스 출력
        print(f'k: {k}')
        for i in range(N):
            print(next_box[i])
        print()

        if is_blue_in:
            continue

        if is_red_in:
            answer = k
            continue

        solution(k + 1, next_box, red=next_red, blue=next_blue, dir_idx=idx)


N, M = map(int, input().split())
box = [list(input()) for _ in range(N)]

answer = 11
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
solution(1, box)
print(answer if answer != 10 else -1)