import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_arr = [0] * (N + 1)
pokemon_dic = {}

for i in range(1, N + 1):
    pokemon = input().rstrip()
    pokemon_arr[i] = pokemon
    pokemon_dic[pokemon] = i

for _ in range(M):
    word = input().rstrip()
    if word.isalpha():
        print(pokemon_dic[word])
    else:
        print(pokemon_arr[int(word)])
