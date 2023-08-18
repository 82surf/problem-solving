import sys
sys.stdin = open('input.txt')

N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

for me in people:
    prize = 1
    for other in people:
        if me != other:
            me_x, me_y = me
            other_x, other_y = other

            if other_x > me_x and other_y > me_y:
                prize += 1
    print(prize, end=" ")