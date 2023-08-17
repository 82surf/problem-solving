import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

card_dic = {}
for card in cards:
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1

for num in nums:
    if num in card_dic:
        print(card_dic[num], end=' ')
    else:
        print(0, end=' ')