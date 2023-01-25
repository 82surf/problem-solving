import sys
sys.stdin = open('input.txt')


def solution(matrix, k):
    global answer

    if k == 5:
        max_val = max(list(map(max, matrix)))
        if answer < max_val:
            answer = max_val
        return

    # 방향을 입력받으면 중력을 적용시키고 최댓값을 반환하는 함수
    def move(d):
        start, end, delta = (0, n, 1) if d == (0, -1) or d == (-1, 0) else (n-1, -1, -1)
        if d == (-1, 0) or d == (1, 0):
            for c in range(start, end, delta):
                ok_to_sum = True
                for r in range(start, end, delta):
                    if next_matrix[r][c]:
                        val = next_matrix[r][c]
                        next_matrix[r][c] = 0
                        next_r, next_c = r, c
                        while n > next_r + d[0] >= 0 == next_matrix[next_r + d[0]][next_c] and n > next_c + d[1] >= 0 == next_matrix[next_r][next_c + d[1]]:
                            next_r += d[0]
                            next_c += d[1]
                        if ok_to_sum and 0 <= next_c + d[1] < n and 0 <= next_r + d[0] < n and val == next_matrix[next_r + d[0]][next_c + d[1]]:
                            next_matrix[next_r + d[0]][next_c + d[1]] = val * 2
                            ok_to_sum = False
                        else:
                            next_matrix[next_r][next_c] = val
                            ok_to_sum = True
        else:
            for r in range(start, end, delta):
                ok_to_sum = True
                for c in range(start, end, delta):
                    if next_matrix[r][c]:
                        val = next_matrix[r][c]
                        next_matrix[r][c] = 0
                        next_r, next_c = r, c
                        while n > next_r + d[0] >= 0 == next_matrix[next_r + d[0]][next_c] and n > next_c + d[1] >= 0 == next_matrix[next_r][next_c + d[1]]:
                            next_r += d[0]
                            next_c += d[1]
                        if ok_to_sum and 0 <= next_c + d[1] < n and 0 <= next_r + d[0] < n and val == next_matrix[next_r + d[0]][next_c + d[1]]:
                            next_matrix[next_r + d[0]][next_c + d[1]] = val * 2
                            ok_to_sum = False
                        else:
                            next_matrix[next_r][next_c] = val
                            ok_to_sum = True

    for d in dirs:
        next_matrix = [row[:] for row in matrix]
        move(d)
        solution(next_matrix, k + 1)


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
solution(matrix, 0)
print(answer)
