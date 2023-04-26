from heapq import heappush, heappop


def solution(n, k, enemy):
    prefix_sum = 0
    skill_sum, skill_cnt = 0, 0
    skill_vals = []

    for i, num in enumerate(enemy):
        prefix_sum += num

        if skill_cnt < k:
            skill_cnt += 1
            skill_sum += num
            heappush(skill_vals, num)
        elif num > skill_vals[0]:
            skill_sum -= heappop(skill_vals)
            heappush(skill_vals, num)
            skill_sum += num

        if prefix_sum - skill_sum > n:
            return i
    else:
        return len(enemy)