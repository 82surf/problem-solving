import sys
sys.stdin = open('input.txt')


def solution(parent, left_c, right_c, k):
    answer[k].append(record[parent])

    if k == K - 1:
        return

    if k < K - 2:
        next_left = (parent + left_c) // 2
        next_right = (right_c + parent) // 2 + 1
        solution(next_left, left_c, parent - 1, k + 1)
        solution(next_right, parent + 1, right_c, k + 1)
    else:
        solution(left_c, 0, 0, k + 1)
        solution(right_c, 0, 0, k + 1)


K = int(input())
buildings = [0 for _ in range(2 ** K - 1)]
record = list(map(int, input().split()))
answer = [[] for _ in range(K)]

root_idx = (2 ** K - 1) // 2
solution(root_idx, 0, 2 ** K - 2, 0)
for ans in answer:
    print(*ans)