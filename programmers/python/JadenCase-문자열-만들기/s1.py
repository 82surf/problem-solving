def solution(s):
    s = list(s)
    for i, c in enumerate(s):
        if c == ' ' or ord(c) < 58:
            pass
        elif i == 0 or s[i - 1] == ' ':
            s[i] = c.upper()
        elif c.isupper():
            s[i] = c.lower()
    return ''.join(s)
