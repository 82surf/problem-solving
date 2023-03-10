# 시간초과
# O(n^2)
def solution(numbers):
    n = len(numbers)
    big_nums = []

    answer = [-1] * n
    for i in range(n - 2, -1, -1):
        if answer[i + 1] == -1:
            if numbers[i] < numbers[i + 1]:
                answer[i] = numbers[i + 1]
                big_nums.append(numbers[i + 1])
        else:
            if numbers[i] < numbers[i + 1]:
                answer[i] = numbers[i + 1]
                big_nums.append(numbers[i + 1])
            else:
                for j in range(len(big_nums) - 1, -1, -1):
                    if numbers[i] < big_nums[j]:
                        answer[i] = big_nums[j]
                        break
    return answer