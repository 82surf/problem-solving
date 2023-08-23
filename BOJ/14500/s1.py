import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]


# 회전, 대칭 시 가로, 세로 2가지 모양
def tetromino_bar():
    max_total = 0
    for i in range(N):
        for j in range(M - 3):
            total_horizontal = 0
            for k in range(4):
                total_horizontal += paper[i][j + k]
            if max_total < total_horizontal:
                max_total = total_horizontal

    for i in range(N - 3):
        for j in range(M):
            total_vertical = 0
            for k in range(4):
                total_vertical += paper[i + k][j]
            if max_total < total_vertical:
                max_total = total_vertical

    return max_total


# 회전, 대칭해도 모양이 동일
def tetromino_square():
    max_total = 0
    for i in range(N - 1):
        for j in range(M - 1):
            total = 0
            for k in range(2):
                total += paper[i][j + k]
                total += paper[i + 1][j + k]
            if max_total < total:
                max_total = total
    return max_total


def tetromino_S():
    max_total = 0
    # 세로로 긴 S자 블럭
    for i in range(N - 2):
        for j in range(M - 1):
            total_1 = 0  # S자 블럭
            total_2 = 0  # S자를 좌우 대칭한 블럭
            for k in range(2):
                total_1 += paper[i + k][j]
                total_1 += paper[i + k + 1][j + 1]

                total_2 += paper[i + k][j + 1]
                total_2 += paper[i + k + 1][j]
            # 최댓값 갱신
            if max_total < total_1:
                max_total = total_1
            if max_total < total_2:
                max_total = total_2
    # 가로로 긴 S자 블럭
    for i in range(N - 1):
        for j in range(M - 2):
            total_3 = 0  # Z자 블럭
            total_4 = 0  # Z자를 좌우 대칭한 블럭
            for k in range(2):
                total_3 += paper[i][j + k]
                total_3 += paper[i + 1][j + k + 1]

                total_4 += paper[i][j + k + 1]
                total_4 += paper[i + 1][j + k]
            # 최댓값 갱신
            if max_total < total_3:
                max_total = total_3
            if max_total < total_4:
                max_total = total_4

    return max_total


def tetromino_L_T():
    max_total = 0

    # 세로로 긴 블럭
    for i in range(N - 2):
        for j in range(M - 1):
            # 왼쪽에 긴 바가 있는 L블럭
            L_left_long_top_toe = paper[i][j + 1]
            L_left_long_bottom_toe = paper[i + 2][j + 1]
            # 왼쪽에 긴 바가 있는 T블럭
            T_left_long = paper[i + 1][j + 1]

            # 오른쪽에 긴 바가 있는 L블럭
            L_right_long_top_toe = paper[i][j]
            L_right_long_bottom_toe = paper[i + 2][j]
            # 오른쪽에 긴 바가 있는 T블럭
            T_right_long = paper[i + 1][j]

            for k in range(3):
                L_left_long_top_toe += paper[i + k][j]
                L_left_long_bottom_toe += paper[i + k][j]
                T_left_long += paper[i + k][j]

                L_right_long_top_toe += paper[i + k][j + 1]
                L_right_long_bottom_toe += paper[i + k][j + 1]
                T_right_long += paper[i + k][j + 1]

            tmp_total = max([L_left_long_top_toe, L_left_long_bottom_toe, L_right_long_top_toe, L_right_long_bottom_toe, T_left_long, T_right_long])
            if max_total < tmp_total:
                max_total = tmp_total

    # 가로로 긴 블럭
    for i in range(N - 1):
        for j in range(M - 2):
            # 위쪽에 긴 바가 있는 L블럭
            L_top_long_left_toe = paper[i + 1][j]
            L_top_long_right_toe = paper[i + 1][j + 2]
            # 위쪽에 긴 바가 있는 T블럭
            T_top_long = paper[i + 1][j + 1]

            # 아래쪽에 긴 바가 있는 L블럭
            L_bottom_long_left_toe = paper[i][j]
            L_bottom_long_right_toe = paper[i][j + 2]
            # 아래쪽에 긴 바가 있는 T블럭
            T_bottom_long = paper[i][j + 1]

            for k in range(3):
                L_top_long_left_toe += paper[i][j + k]
                L_top_long_right_toe += paper[i][j + k]
                T_top_long += paper[i][j + k]

                L_bottom_long_left_toe += paper[i + 1][j + k]
                L_bottom_long_right_toe += paper[i + 1][j + k]
                T_bottom_long += paper[i + 1][j + k]

            tmp_total = max(L_top_long_left_toe, L_top_long_right_toe, L_bottom_long_left_toe, L_bottom_long_right_toe, T_top_long, T_bottom_long)
            if max_total < tmp_total:
                max_total = tmp_total

    return max_total


print(max(tetromino_bar(), tetromino_S(), tetromino_square(), tetromino_L_T()))
