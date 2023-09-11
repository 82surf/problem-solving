import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
mapper = {}
for _ in range(N):
    url, password = input().split()
    mapper[url] = password
for _ in range(M):
    print(mapper[input().rstrip()])