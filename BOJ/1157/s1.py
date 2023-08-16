word = input().lower()
chr_cnt = [0] * 26
for c in word:
    chr_cnt[ord(c) - 97] += 1

max_val = max(chr_cnt)
if chr_cnt.count(max_val) > 1:
    print('?')
else:
    print(chr(chr_cnt.index(max_val) + 97).upper())