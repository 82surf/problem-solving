# 누적합 + 투포인터

def get_part_sum(prefix_sum, start, end):
    return prefix_sum[end + 1] - prefix_sum[start]


def solution(sequence, k):
    n = len(sequence)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + sequence[i]

    l, r = 0, 0
    answer = None
    part_sum = get_part_sum(prefix_sum, l, r)
    while True:
        if part_sum < k:
            r += 1
        elif part_sum == k:
            if answer is None:
                answer = [l, r]
            else:
                curr_len = r - l
                ans_len = answer[1] - answer[0]
                if curr_len < ans_len:
                    answer = [l, r]
            r += 1
        else:
            l += 1

        if l >= n or r >= n:
            break

        part_sum = get_part_sum(prefix_sum, l, r)

    return answer