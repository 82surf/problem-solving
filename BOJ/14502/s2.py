# python 3 시간초과
# pypy3 통과

from itertools import product
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lab_origin = [list(map(int, input().split())) for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answer = 0

# 바이러스 위치 탐색
virus = []
for n, m in product(range(N), range(M)):
    if lab_origin[n][m] == 2:
        virus.append((n, m))

# 벽 3개 세우기
for n1, m1 in product(range(N), range(M)):
    if lab_origin[n1][m1] == 0:
        for n2, m2 in product(range(N), range(M)):
            if lab_origin[n2][m2] == 0 and (n1, m1) != (n2, m2):
                for n3, m3 in product(range(N), range(M)):
                    if lab_origin[n3][m3] == 0 and (n2, m2) != (n3, m3) and (n1, m1) != (n3, m3):
                        lab = [arr[:] for arr in lab_origin]
                        lab[n1][m1], lab[n2][m2], lab[n3][m3] = 1, 1, 1

                        # 바이러스를 퍼뜨리는 함수
                        def dfs(n, m):
                            lab[n][m] = 2
                            for d in dirs:
                                next_n, next_m = n + d[0], m + d[1]
                                if 0 <= next_n < N and 0 <= next_m < M and lab[next_n][next_m] == 0:
                                    dfs(next_n, next_m)

                        # 바이러스 퍼트리기
                        for vn, vm in virus:
                            dfs(vn, vm)

                        # 안전 영역 탐색
                        cnt = 0
                        for i in range(N):
                            for j in range(M):
                                if lab[i][j] == 0:
                                    cnt += 1
                        if answer < cnt:
                            answer = cnt

print(answer)
