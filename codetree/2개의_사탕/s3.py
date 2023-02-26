from copy import deepcopy
from collections import deque
import sys
sys.stdin = open('input.txt')

# 행, 열, 상자 입력받기
N, M = map(int, input().split())
box = [list(input()) for _ in range(N)]


# 출구 위치 찾기
def search_target():
    red, blue = None, None
    for i in range(N):
        for j in range(M):
            if box[i][j] == 'R':
                red = (i, j)
            if box[i][j] == 'B':
                blue = (i, j)
            if box[i][j] == 'O':
                out = (i, j)
    return red, blue


# 어느 사탕부터 움직일지 결정
def is_red_first(red, blue, dir):
    if dir == (0, 1):
        return True if red[1] - blue[1] > 0 else False
    elif dir == (0, -1):
        return True if blue[1] - red[1] > 0 else False
    elif dir == (1, 0):
        return True if red[0] - blue[0] > 0 else False
    elif dir == (-1, 0):
        return True if blue[0] - red[0] > 0 else False


# 중력 적용하기
# 끝까지 가거나 out에 들어가거나
def gravity(coord, dir, box):
    r, c = coord
    val = box[r][c]
    box[r][c] = '.'
    while True:
        r, c = r + dir[0], c + dir[1]
        if box[r][c] == 'O':
            return True, None
        if not (0 < r <= N and 0 < c <= M and box[r][c] == '.'):
            break
    box[r - dir[0]][c - dir[1]] = val
    return False, (r - dir[0], c - dir[1])


start_red, start_blue = search_target()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# # 4방향 순회하면서 중력 적용
# # 들어갔는지 검사
def BFS():
    q = deque([(start_red, start_blue, box, 0, None)])
    while q:
        now_r, now_b, now_box, cnt, before_d = q.popleft()
        if cnt == 11:
            break
        for d in dirs:
            copy_box = deepcopy(now_box)
            if d == before_d:
                continue
            if is_red_first(now_r, now_b, d):
                is_red_in, next_red = gravity(now_r, d, copy_box)
                is_blue_in, next_blue = gravity(now_b, d, copy_box)
            else:
                is_blue_in, next_blue = gravity(now_b, d, copy_box)
                is_red_in, next_red = gravity(now_r, d, copy_box)
            if now_r == next_red and now_b == next_blue:
                continue
            elif is_blue_in:
                continue
            elif is_red_in:
                result = cnt + 1
                return result if result < 11 else -1
            else:
                q.append((next_red, next_blue, deepcopy(copy_box), cnt + 1, d))
    return -1


print(BFS())