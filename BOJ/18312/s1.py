def sec_to_str(sec):
    h = sec // 3600
    if h:
        sec -= h * 3600
    h = str(h).zfill(2)

    m = sec // 60
    if m:
        sec -= m * 60
    m = str(m).zfill(2)
    sec = str(sec).zfill(2)
    return h + m + sec


N, K = input().split()
total_sec = (int(N) + 1) * 60 * 60
answer = 0
for i in range(total_sec):
    t = sec_to_str(i)
    if K in t:
        answer += 1
print(answer)