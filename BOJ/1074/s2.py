import sys
sys.stdin = open('input.txt')

n, r, c = map(int, input().split())
N = 2 ** n


def check_quadrant(r, c, cr, cc):
    if r < cr and c < cc:
        return 1
    elif r < cr and c >= cc:
        return 2
    elif r >= cr and c < cc:
        return 3
    else:
        return 4


def calc(n, point_to_check, start_point):
    next_n = n // 2
    pr, pc = point_to_check
    sr, sc = start_point
    cr, cc = sr + next_n, sc + next_n

    quadrant = check_quadrant(pr, pc, cr, cc)

    next_sr, next_sc = start_point
    if quadrant == 2:
        next_sc += next_n
    elif quadrant == 3:
        next_sr += next_n
    elif quadrant == 4:
        next_sr += next_n
        next_sc += next_n
    return (next_n ** 2) * (quadrant - 1), (next_sr, next_sc)


answer = 0
start_point = (0, 0)
while N != 1:
    cnt, next_start_point = calc(N, (r, c), start_point)
    answer += cnt
    start_point = next_start_point
    N //= 2

print(answer)