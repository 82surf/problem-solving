# 누적합
# 테스트 케이스 통과, 제출 시 시간 초과
# 짧은 길이 먼저 확인하도록 변경
# 하지만 O(N^2)인 것은 동일

def get_part_sum(prefix_sum, start, end):
    return prefix_sum[end + 1] - prefix_sum[start]


def solution(sequence, k):
    prefix_sum = [0] * (len(sequence) + 1)
    for i in range(len(sequence)):
        prefix_sum[i + 1] = prefix_sum[i] + sequence[i]

    for l in range(len(sequence)):
        for start in range(0, len(sequence) - l):
            end = start + l

            part_sum = get_part_sum(prefix_sum, start, end)
            if part_sum == k:
                return [start, end]