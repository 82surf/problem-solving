import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
classroom = [[0 for _ in range(N)] for _ in range(N)]
likes = [[] for _ in range(N ** 2 + 1)]
students = []
for _ in range(N ** 2):
    student, *like = map(int, input().split())
    students.append(student)
    likes[student] += like

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 학생 순서대로 자리 배치
for student in students:
    # 이 학생의 자리 및 자리 정보
    # like_cnt, empty_cnt, r, c
    seat = (0, 0, N ** 2, N ** 2)

    # 자리 순회
    for r in range(N):
        for c in range(N):
            # 빈 자리에서 조건에 맞는지 탐색
            if not classroom[r][c]:
                like_cnt, empty_cnt = 0, 0
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if classroom[nr][nc] in likes[student]:
                            like_cnt += 1
                        elif not classroom[nr][nc]:
                            empty_cnt += 1
                curr_seat = (like_cnt, empty_cnt, r, c)
                if seat[0] < curr_seat[0]:
                    seat = curr_seat
                elif seat[0] == curr_seat[0]:
                    if seat[1] < curr_seat[1]:
                        seat = curr_seat
                    elif seat[1] == curr_seat[1]:
                        if seat[2] > curr_seat[2]:
                            seat = curr_seat
                        elif seat[2] == curr_seat[2] and seat[3] > curr_seat[3]:
                            seat = curr_seat

    classroom[seat[2]][seat[3]] = student

# 만족도 계산
answer = 0
for r in range(N):
    for c in range(N):
        student = classroom[r][c]
        like_cnt = 0
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                near_student = classroom[nr][nc]
                if near_student in likes[student]:
                    like_cnt += 1
        answer += 10 ** (like_cnt - 1) if like_cnt else 0

print(answer)