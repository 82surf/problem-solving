def solution(word):
    chars = ['A', 'E', 'I', 'O', 'U']
    tmp = [''] * 5
    cnt = 0

    for c in chars:
        tmp[0] = c
        cnt += 1
        if ''.join(tmp[0]) == word:
            return cnt
        for c in chars:
            tmp[1] = c
            cnt += 1
            if ''.join(tmp[:2]) == word:
                return cnt
            for c in chars:
                tmp[2] = c
                cnt += 1
                if ''.join(tmp[:3]) == word:
                    return cnt
                for c in chars:
                    tmp[3] = c
                    cnt += 1
                    if ''.join(tmp[:4]) == word:
                        return cnt
                    for c in chars:
                        tmp[4] = c
                        cnt += 1
                        if ''.join(tmp) == word:
                            return cnt
