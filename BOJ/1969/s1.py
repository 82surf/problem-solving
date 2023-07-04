import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
dna_list = [input() for _ in range(N)]
answer_dna = ''
answer_dist = 0

for i in range(M):
    ACGT = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for dna in dna_list:
        if dna[i] == 'A':
            ACGT['A'] += 1
        elif dna[i] == 'C':
            ACGT['C'] += 1
        elif dna[i] == 'G':
            ACGT['G'] += 1
        else:
            ACGT['T'] += 1

    max_key, max_val = 'A', 0
    for key, val in ACGT.items():
        if max_val < val:
            max_key = key
            max_val = val
    answer_dna += max_key

    for dna in dna_list:
        if dna[i] != max_key:
            answer_dist += 1

print(answer_dna)
print(answer_dist)
