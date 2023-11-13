def check_bracket(s):
    stack = []
    pair = { '[': ']', '(': ')', '{': '}'}
    for c in s:
        if stack and stack[-1] in pair and c == pair[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    return True if not stack else False

def solution(s):
    answer = 0
    for _ in range(len(s)):
        s = s[1:] + s[:1]
        if check_bracket(s):
            answer += 1
    return answer