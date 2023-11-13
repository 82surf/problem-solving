def solution(n):
    # 입력해야할 수: 1부터 n까지의 합만큼
    num = n * (n + 1) // 2

    # 1
    # 2 6
    # 3 4 5
    # 삼각형을 의미하는 2차원 배열 선언
    triangle = [[0] * n for _ in range(n)]

    # 입력 방향
    dirs = [(1, 0), (0, 1), (-1, -1)]
    # 방향을 나타낼 플래그
    dir_idx = 0
    # 초기 위치
    r, c = -1, 0
    # 입력할 값
    val = 1
    # num까지 입력하면 반복 종료
    while val <= num:
        dr, dc = dirs[dir_idx % 3]
        nr, nc = r + dr, c + dc
        # 다음 탐색 좌표가 비어있으면 입력
        if 0 <= nr < n and 0 <= nc < n and not triangle[nr][nc]:
            r, c = nr, nc
            triangle[r][c] = val
            val += 1
        # 아니면 방향 전환
        else:
            dir_idx += 1

    # 정답 배열 선언
    answer = [0] * num

    # 삼각형을 순회하면서 값이 있으면 정답 배열 채우기
    idx = 0
    for i in range(n):
        for j in range(n):
            if triangle[i][j]:
                answer[idx] = triangle[i][j]
                idx += 1
    return answer