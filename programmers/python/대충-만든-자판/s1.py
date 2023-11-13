def solution(keymap, targets):
    min_keymap = {}
    for i in range(65, 91):
        key = chr(i)
        min_keymap[key] = min_keymap.get(key, 101)

    for k in keymap:
        for i, c in enumerate(k):
            if min_keymap[c] > i:
                min_keymap[c] = i + 1

    answer = [0] * len(targets)
    for i, t in enumerate(targets):
        cnt = 0
        for c in t:
            if min_keymap[c] <= 100:
                cnt += min_keymap[c]
        answer[i] = cnt if cnt else -1

    return answer
