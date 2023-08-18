import sys
input = sys.stdin.readline

T = int(input())
k_arr, n_arr = [0] * T, [0] * T
for t in range(T):
    k_arr[t] = int(input())
    n_arr[t] = int(input())

# 아파트 초기화
max_k, max_n = max(k_arr), max(n_arr)
apartment = [[0] * max_n for _ in range(max_k + 1)]
for i in range(1, max_n + 1):
    apartment[0][i-1] = i

# 아파트 입주민 채우기
for i in range(1, max_k + 1):
    for j in range(max_n):
        apartment[i][j] = sum(apartment[i-1][:j + 1])

# 정답 출력
for t in range(T):
    print(apartment[k_arr[t]][n_arr[t] - 1])