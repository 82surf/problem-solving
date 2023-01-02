import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    answers = input()
    score = 1
    total = 0
    for ans in answers:
        if ans == 'O':
            total += score
            score += 1
        else:
            score = 1
    print(total)