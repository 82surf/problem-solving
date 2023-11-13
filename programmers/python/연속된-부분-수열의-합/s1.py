# 누적합
# 테스트 케이스 통과, 제출 시 시간 초과

def get_part_sum(prefix_sum, start, end):
    return prefix_sum[end + 1] - prefix_sum[start]


def solution(sequence, k):
    prefix_sum = [0] * (len(sequence) + 1)
    for i in range(len(sequence)):
        prefix_sum[i + 1] = prefix_sum[i] + sequence[i]

    answer = None
    # 이 부분이 O(N^2)로 시간초과의 원인인 듯
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            part_sum = get_part_sum(prefix_sum, i, j)
            if part_sum == k:
                if answer is None:
                    answer = (i, j)
                else:
                    curr_len = j - i
                    ans_len = answer[1] - answer[0]
                    if curr_len < ans_len:
                        answer = (i, j)
    return answer