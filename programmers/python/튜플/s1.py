def solution(s):
    set_li = s[2:-2].split('},{')
    set_li = sorted(map(lambda x: set(x.split(',')), set_li), key=lambda x: len(x))

    answer = []
    for i in range(len(set_li)):
        item = set_li[i] - set_li[i - 1] if i else set_li[i]
        answer.append(int(list(item)[0]))

    return answer