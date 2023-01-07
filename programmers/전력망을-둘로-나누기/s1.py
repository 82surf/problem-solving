def DFS(s, edges):
    visited = []
    stack = [s]
    cnt = 0
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            cnt += 1
            for w in edges[v]:
                stack.append(w)
    return cnt


def solution(n, wires):
    edges = [[] for _ in range(n + 1)]
    for w in wires:
        edges[w[0]].append(w[1])
        edges[w[1]].append(w[0])

    ans = 100

    for i in range(len(wires)):
        wires_cut = wires[:i] + wires[i + 1:]
        edges = [[] for _ in range(n + 1)]
        for w in wires_cut:
            edges[w[0]].append(w[1])
            edges[w[1]].append(w[0])

        cnt = DFS(wires_cut[0][0], edges)
        diff = abs(cnt * 2 - n)

        if ans >= diff:
            ans = diff

    return ans

