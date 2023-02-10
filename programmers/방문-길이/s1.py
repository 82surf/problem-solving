def solution(dirs):
    answer = 0
    board = [[0] * 21 for _ in range(21)]
    r, c = 10, 10
    coord = { 'R': (2, 0), 'L': (-2, 0), 'U': (0, -2), 'D': (0, 2) }
    for d in dirs:
        delta_r, delta_c = coord[d][0], coord[d][1]
        next_r, next_c = r + delta_r, c + delta_c
        road_r, road_c = r + delta_r // 2, c + delta_c //2
        if 0 <= next_r < 21 and 0 <= next_c < 21:
            if not board[road_r][road_c]:
                board[road_r][road_c] = 1
                answer += 1
            r, c = next_r, next_c
    return answer