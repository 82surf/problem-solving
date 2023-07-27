import sys
sys.stdin = open('input.txt')


def check(a, b):
    return 'ascending' if b - a > 0 else 'descending'


def solution(arr):
    result = check(arr[0], arr[1])
    for i in range(2, len(arr)):
        if check(arr[i - 1], arr[i]) != result:
            return 'mixed'
    return result


def main():
    DCT = list(map(int, input().split()))
    print(solution(DCT))


main()