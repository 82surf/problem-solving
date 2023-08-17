import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
users = [0] * N
for i in range(N):
    age_str, name = input().split()
    age = int(age_str)
    users[i] = (i, age, name)
users.sort(key=lambda user: (user[1], user[0]))
for i, age, name in users:
    print(age, name)