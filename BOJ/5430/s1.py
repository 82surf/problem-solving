from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    command_arr = list(input().rstrip())
    N = int(input())
    num_input = input().rstrip()
    num_arr = []
    if num_input != '[]':
        num_arr = deque(list(map(int, num_input[1:-1].split(','))))

    is_reversed = False

    def R():
        global is_reversed
        is_reversed = not is_reversed

    def D():
        num_arr.pop() if is_reversed else num_arr.popleft()

    def get_result():
        search_range = (len(num_arr) - 1, -1, -1) if is_reversed else (0, len(num_arr))
        result = '['
        for i in range(*search_range):
            result += str(num_arr[i])
            if (is_reversed and i != 0) or (not is_reversed and i != len(num_arr) - 1):
                result += ','

        return result + ']'

    def run_command():
        for command in command_arr:
            if command == 'R':
                R()
            elif command == 'D':
                if num_arr:
                    D()
                else:
                    return 'error'
        return get_result()

    print(run_command())