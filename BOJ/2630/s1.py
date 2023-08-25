import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


def erase(r, c, w):
    for i in range(w):
        for j in range(w):
            paper[r + i][c + j] = -1


def check(r, c, w, val):
    for i in range(w):
        for j in range(w):
            if paper[r + i][c + j] != val:
                return False
    return True


def solution(width):
    blue_paper = 0
    white_paper = 0

    for start_r in range(0, N, width):
        for start_c in range(0, N, width):
            curr = paper[start_r][start_c]
            if curr >= 0 and check(start_r, start_c, width, curr):
                erase(start_r, start_c, width)
                if curr == 1:
                    blue_paper += 1
                else:
                    white_paper += 1

    return blue_paper, white_paper


width = N
total_blue, total_white = solution(width)
while width > 1:
    width //= 2
    blue, white = solution(width)
    total_blue += blue
    total_white += white

print(total_white)
print(total_blue)