import sys
sys.stdin = open('input.txt')


def check(string):
    stack = []

    def push(p):
        if not stack:
            stack.append(p)
        elif p == ")" and stack[-1] == "(":
            stack.pop()
        elif p == "]" and stack[-1] == "[":
            stack.pop()
        else:
            stack.append(p)

    for s in string:
        if s in ["(", ")", "[", "]"]:
            push(s)

    return 'yes' if not stack else 'no'


while True:
    sentence = input()
    if sentence == '.':
        break
    print(check(sentence))