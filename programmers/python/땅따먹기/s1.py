def solution(land):
    answer = [0] * 4
    for nums in land:
        tmp = [0] * 4
        for i, n in enumerate(answer):
            tmp[i] = (n, i)
        tmp.sort(reverse=True, key=lambda x: x[0])
        first, second = tmp[0], tmp[1]

        for i in range(4):
            answer[i] = first[0] + nums[i] if i != first[1] else second[0] + nums[i]
    return max(answer)
