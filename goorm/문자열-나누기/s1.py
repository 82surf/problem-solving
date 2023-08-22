import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = input().rstrip()

P = []  # P 배열 초기화
P_dic = {}  # 중복 확인을 위한 해시테이블
candidates = []  # 점수를 확인할 3개의 문자열 목록

for i, j in combinations(range(1, N), 2):  # 조합으로 P 배열 채우기
    a, b, c = S[:i], S[i:j], S[j:]
    candidates.append((a, b, c))
    for w in [a, b, c]:
        if w not in P_dic:
            P_dic[w] = 1
            P.append(w)

P.sort()  # P 배열 정렬

score_board = {}  # O(1)로 점수를 확인하기 위한 해시테이블
for i, w in enumerate(P):
    score_board[w] = i + 1

# 최고 점수 탐색
max_score = 0
for a, b, c in candidates:
    score = score_board[a] + score_board[b] + score_board[c]
    if max_score < score:
        max_score = score

print(max_score)
