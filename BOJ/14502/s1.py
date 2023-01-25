import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
lab_origin = [list(map(int, input().split())) for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answer = 0
virus = []
for i in range(N):
    for j in range(M):
        if lab_origin[i][j] == 2:
            virus.append((i, j))

for n1 in range(N):
    for m1 in range(M):
        if lab_origin[n1][m1] == 0:
            for n2 in range(N):
                for m2 in range(M):
                    if lab_origin[n2][m2] == 0 and (n1, m1) != (n2, m2):
                        for n3 in range(N):
                            for m3 in range(M):
                                if lab_origin[n3][m3] == 0 and (n2, m2) != (n3, m3) and (n1, m1) != (n3, m3):
                                    # n1, m1 = 0, 1
                                    # n2, m2 = 1, 0
                                    # n3, m3 = 0, 2
                                    lab = [arr[:] for arr in lab_origin]
                                    lab[n1][m1] = 1
                                    lab[n2][m2] = 1
                                    lab[n3][m3] = 1

                                    # 3개의 벽 세우기
                                    # 바이러스 퍼트리기
                                    def dfs(n, m):
                                        lab[n][m] = 2
                                        for d in dirs:
                                            next_n, next_m = n + d[0], m + d[1]
                                            if 0 <= next_n < N and 0 <= next_m < M and lab[next_n][next_m] == 0:
                                                dfs(next_n, next_m)

                                    for vn, vm in virus:
                                        dfs(vn, vm)

                                    cnt = 0
                                    for i in range(N):
                                        for j in range(M):
                                            if lab[i][j] == 0:
                                                cnt += 1

                                    if answer < cnt:
                                        answer = cnt


print(answer)