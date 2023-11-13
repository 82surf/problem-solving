def solution(r1, r2):
    def get_cnt(r):
        cnt = 0
        border_cnt = 0
        x, y = 1, r - 1

        while x <= r - 1:
            a = x ** 2 + y ** 2
            b = r ** 2
            if a <= b:
                cnt += y
                x += 1
                if a == b:
                    border_cnt += 1
            else:
                y -= 1

        return (cnt * 4) + ((r - 1) * 4) + 1, border_cnt * 4 + 4

    r1_cnt, r1_border_cnt = get_cnt(r1)
    r2_cnt, r2_border_cnt = get_cnt(r2)

    return r2_cnt - r1_cnt + r1_border_cnt