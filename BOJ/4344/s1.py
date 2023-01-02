import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    N, scores, = arr[0], arr[1:]
    avg = sum(scores) / N
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    print(f'{cnt/N*100:.3f}%')
