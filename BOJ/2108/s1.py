import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * N
nums_dic = {}
max_cnt = 0
max_n = -4001
min_n = 4001
for i in range(N):
    n = int(input())
    # 숫자 기록
    nums[i] = n
    # 횟수 기록
    if n in nums_dic:
        nums_dic[n] += 1
    else:
        nums_dic[n] = 1

    if max_cnt < nums_dic[n]:
        max_cnt = nums_dic[n]

    # 최댓값, 최솟값 기록
    if max_n < n:
        max_n = n
    if min_n > n:
        min_n = n
nums.sort()

print(round(sum(nums) / N))
print(nums[N // 2])


def get_mode():
    mode_arr = []
    for n, cnt in nums_dic.items():
        if cnt == max_cnt:
            mode_arr.append(n)
    mode_arr.sort()
    if len(mode_arr) > 1:
        return mode_arr[1]
    else:
        return mode_arr[0]

print(get_mode())
print(max_n - min_n)