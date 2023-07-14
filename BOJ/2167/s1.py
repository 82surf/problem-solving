import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 2차원 배열 입력받기
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 누적합 만들기
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for r in range(1, N + 1):
    for c in range(1, M + 1):
        prefix_sum[r][c] = matrix[r-1][c-1] + prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    answer = prefix_sum[x][y] - prefix_sum[x][j-1] - prefix_sum[i-1][y] + prefix_sum[i-1][j-1]
    print(answer)