def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes:
        size.sort()
        if size[0] > max_h:
            max_h = size[0]
        if size[1] > max_w:
            max_w = size[1]
    answer = max_w * max_h
    return answer