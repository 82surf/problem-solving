def solution(elements):
    N = len(elements)
    elements += elements
    sum_set = set()
    for search_len in range(1, N + 1):
        for start_idx in range(N):
            sum_set.add(sum(elements[start_idx:start_idx + search_len]))
    return len(sum_set)
