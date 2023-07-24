from math import inf
from itertools import combinations
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집, 치킨집 위치 저장
houses, chicken_places = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken_places.append((i, j))


def calculate_chicken_dist(house_loc, chicken_loc):
    hx, hc = house_loc
    cx, cc = chicken_loc
    return abs(hx - cx) + abs(hc - cc)


def min_chicken_dist(house, chicken_places):
    dist_arr = []
    for place in chicken_places:
        dist_arr.append(calculate_chicken_dist(house, place))
    return min(dist_arr)


answer = inf
for chosen_chicken_places in combinations(chicken_places, M):
    total_chicken_dist = 0
    for house in houses:
        total_chicken_dist += min_chicken_dist(house, chosen_chicken_places)

    if answer > total_chicken_dist:
        answer = total_chicken_dist

print(answer)
