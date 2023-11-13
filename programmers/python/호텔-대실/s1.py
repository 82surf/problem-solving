def hour_to_min(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def arr_to_min(arr):
    return list(map(hour_to_min, arr))

def solution(book_time):
    book_minute = sorted(list(map(arr_to_min, book_time)))
    rooms = { 1: [] }
    room_num = 2
    for start, end in book_minute:
        for stack in rooms.values():
            if not stack:
                stack.append((start, end))
                break
            elif stack[-1][-1] + 10 <= start:
                stack.append((start, end))
                break
        else:
            rooms[room_num] = [(start, end)]
            room_num += 1
    return len(rooms)