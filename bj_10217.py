import sys

input = sys.stdin.readline
inf = sys.maxsize

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dp = [[inf] * (m + 1) for _ in range(n + 1)]

    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append([v, c, d])
    
    dp[1][0] = 0

    for c in range(m + 1):
        for d in range(1, n + 1):
            if dp[d][c] == inf:
                continue
            t = dp[d][c]
            for dv, dc, dd in graph[d]:
                if dc + c > m:
                    continue
                dp[dv][dc + c] = min(dp[dv][dc + c], t + dd)

    result = min(dp[n])

    if result == inf:
        print("Poor KCM")
    else:
        print(result)

