import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

# N: 학생의 수
# K: 졸고 있는 학생의 수
# Q: 출석 코드를 보낼 학생의 수
# M: 주어질 구간의 수
N, K, Q, M = map(int, input().split())
sleeping_students = list(map(int, input().split()))
messenger_students = list(map(int, input().split()))

# 메시지 보내기
students = [1] * (N + 3)
for ms in messenger_students:
    if ms not in sleeping_students:
        idx = ms
        while idx <= N + 2:
            students[idx] = 0
            idx += ms
# 졸고 있는 학생 제외하기
for ss in sleeping_students:
    students[ss] = 1
# 누적합 구하기
prefix_sum = [0] * (N + 3)
for i in range(3, N + 3):
    if i == 3:
        prefix_sum[i] = students[i]
    else:
        prefix_sum[i] = students[i] + prefix_sum[i-1]
for _ in range(M):
    S, E = map(int, input().split())
    print(prefix_sum[E] - prefix_sum[S - 1])

