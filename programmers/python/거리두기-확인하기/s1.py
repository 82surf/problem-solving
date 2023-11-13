def solution(places):
    answer = [1] * 5

    def DFS(start, before, place, visited, ans_i, dist):
        nonlocal answer

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = before
        visited[r][c] = 1

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                if place[nr][nc] == 'P':
                    answer[ans_i] = 0
                    return
                elif place[nr][nc] == 'O':
                    if dist <= 1:
                        DFS(start, (nr, nc), place, visited, ans_i, dist + 1)

    for i, place in enumerate(places):
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    visited = [[0] * 5 for _ in range(5)]
                    DFS((r, c), (r, c), place, visited, i, 1)

    return answer
