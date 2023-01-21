import sys
sys.stdin = open('inputl.txt')


def b_search(arr, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))
answer = [0 for _ in range(M)]

for i in range(M):
    n = nums[i]
    answer[i] = b_search(cards, n)

print(*answer)