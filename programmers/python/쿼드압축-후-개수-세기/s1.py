def solution(arr):
    answer = [0, 0]

    # 압축 길이만큼 순회하며 검사
    # 압축 가능 => 0, 1 개수 올리고 함수 종료
    # 압축 불필요 => 재귀
    def quad_compress(cmp_arr):
        nonlocal answer

        if len(cmp_arr) == 1:
            answer[cmp_arr[0][0]] += 1
            return

        # 순회할 길이는 배열의 절반
        l = len(cmp_arr) // 2
        # 시작 지점 초기화
        starts = [(0, 0), (l, 0), (0, l), (l, l)]
        # 시작 지점부터
        for r, c in starts:
            # 순회할 길이만큼 2차원 배열 탐색
            for i in range(l):
                is_stopped = False
                for j in range(l):
                    nr, nc = r + i, c + j
                    # 탐색 중 다른 수가 나오면 탐색을 멈추고 재귀
                    if cmp_arr[r][c] != cmp_arr[nr][nc]:
                        is_stopped = True
                        next_part = [arr[c:c + l] for arr in cmp_arr[r:r + l]]
                        quad_compress(next_part)
                        break
                        return
                if is_stopped:
                    break
            # 다른 수가 나오지 않으면 0, 1의 개수 추가
            else:
                answer[cmp_arr[r][c]] += 1

    def check_arr():
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[0][0] != arr[i][j]:
                    return False
        return True

    if check_arr():
        answer[arr[0][0]] += 1
    else:
        quad_compress(arr)

    return answer