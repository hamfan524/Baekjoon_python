import sys
from heapq import heappush,heappop, heappushpop

input = sys.stdin.readline
inf = sys.maxsize

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [[False] * (K + 1) for _ in range(N + 1)]
dp =[[inf] * (K + 1) for _ in range(N + 1)]
heap = []

def dijkstra():
    heappush(heap, [1, 1, K])

    for i in range(K + 1):
        dp[1][i] = 0

    while heap:
        w, n, k = heappop(heap)

        if visit[n][k]:
            continue
        visit[n][k] = True
        for n_n, wei in graph[n]:
            if dp[n][k] + wei < dp[n_n][k]:
                dp[n_n][k] = dp[n][k] + wei
                heappush(heap, [dp[n_n][k] , n_n, k])
            if k > 0:
                if dp[n_n][k-1] > dp[n][k]:
                    dp[n_n][k-1] = dp[n][k]
                heappush(heap, [dp[n_n][k-1], n_n, k - 1])

for _ in range(M):
    c1, c2, t = map(int, input().split())
    graph[c1].append([c2, t])
    graph[c2].append([c1, t])

dijkstra()

print(min(dp[-1]))