# 균형잡힌 괄호인지 확인
def is_balanced(s):
    return s.count('(') == s.count(')')


# 올바른 괄호인지 확인
def is_right(s):
    stack = []
    for c in s:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
        else:
            stack.append(c)
    return True if not stack else False


# w를 u(균형)와 v로 분리
def split_p(p):
    for i in range(1, len(p) + 1):
        if is_balanced(p[:i]):
            return p[:i], p[i:]


# 괄호 뒤집기
def reverse_p(p):
    result = ''
    for c in p:
        result += '(' if c == ')' else ')'
    return result


def solution(p):
    # 1.
    if not p or is_right(p):
        return p

    # 2.
    u, v = split_p(p)

    # 3.
    if is_right(u):
        return u + solution(v)
    # 4.
    else:
        a = '(' + solution(v) + ')'
        b = reverse_p(u[1:-1])
        return a + b