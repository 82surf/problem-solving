import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A_dic = {}
for a in A:
    A_dic[a] = 1

for num in nums:
    if num in A_dic:
        print(1)
    else:
        print(0)