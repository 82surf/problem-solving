from itertools import permutations


def calculate(exp_arr, priority):
    stack = []
    p_idx = 0
    for i in exp_arr:
        if not stack:
            stack.append(i)
        elif priority[p_idx] == stack[-1]:
            val = None
            if stack[-1] == '+':
                val = stack[-2] + i
            elif stack[-1] == '-':
                val = stack[-2] - i
            else:
                val = stack[-2] * i
            stack.pop()
            stack.pop()
            stack.append(val)
        else:
            stack.append(i)

    if len(stack) == 1:
        return stack[0]

    return calculate(stack, priority[1:])


def solution(expression):
    # 식 배열로 변환 & 연산자 set 생성
    oprs = set()
    exp_arr = []
    tmp = ''
    for c in expression:
        if c.isdigit():
            tmp += c
        else:
            exp_arr.append(int(tmp))
            tmp = ''
            exp_arr.append(c)
            oprs.add(c)
    else:
        exp_arr.append(int(tmp))

        # 계산 우선순위 완전 탐색
    answer = 0
    for p in permutations(list(oprs), len(oprs)):
        val = abs(calculate(exp_arr, p))
        if answer < val:
            answer = val
    return answer

