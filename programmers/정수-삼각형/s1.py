def solution(triangle):
    for i, arr in enumerate(triangle):
        for j, n in enumerate(arr):
            if i == 0 and j == 0:
                pass
            elif j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(arr) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            elif i > 0 and j > 0:
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

    return max(triangle[-1])