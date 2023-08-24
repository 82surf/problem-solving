import sys
input = sys.stdin.readline

# 입력받기
T = int(input())
n_arr = [int(input()) for _ in range(T)]

# n 최댓값에 맞춰 배열 생성
max_n = max(n_arr)
if max_n < 2:
    max_n = 2

arr_0 = [0] * (max_n + 1)
arr_0[0], arr_0[1], arr_0[2] = 1, 0, 1

arr_1 = [0] * (max_n + 1)
arr_1[0], arr_1[1], arr_1[2] = 0, 1, 1

# 배열 채우기
for i in range(3, max_n + 1):
    arr_0[i] = arr_0[i - 1] + arr_0[i - 2]
    arr_1[i] = arr_1[i - 1] + arr_1[i - 2]

# 정답 출력
for n in n_arr:
    print(arr_0[n], arr_1[n])