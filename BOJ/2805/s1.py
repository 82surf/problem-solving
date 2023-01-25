import sys
sys.stdin = open('input.txt')


def cut_tree(cut):
    total = 0
    for tree in trees:
        total += tree - cut if tree > cut else 0
    return total


def b_search(start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        amount = cut_tree(mid)

        if M < amount:
            start = mid + 1
            answer = mid
        elif M == amount:
            answer = mid
            break
        else:
            end = mid - 1



N, M = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0
b_search(0, max(trees))
print(answer)