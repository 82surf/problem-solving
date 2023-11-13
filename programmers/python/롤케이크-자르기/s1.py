def solution(topping):
    part1 = {}
    for t in topping:
        if t in part1:
            part1[t] += 1
        else:
            part1[t] = 1

    answer = 0
    part2 = {}
    for t in topping:
        part1[t] -= 1
        if not part1[t]:
            part1.pop(t)

        if t in part2:
            part2[t] += 1
        else:
            part2[t] = 1

        if len(part1) == len(part2):
            answer += 1

    return answer