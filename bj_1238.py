import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m, x = map(int, input().split())
inf = sys.maxsize
graph = [[] for _ in range(n + 1)]
dp = [inf] * (n + 1)
graph_r = [[] for _ in range(n + 1)]
dp_r = [inf] * (n + 1)

def dijkstra(start, dp, graph):
    heap = []
    heappush(heap, [0, start])
    dp[start] = 0
    while heap:
        w, n = heappop(heap)
        if dp[n] < w:
            continue
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

for i in range(m):
    d, a, t = map(int, input().split())
    graph[d].append([a, t])
    graph_r[a].append([d, t])

dijkstra(x, dp, graph)
dijkstra(x, dp_r, graph_r)

max_ = 0
for i in range(1, n + 1):
    max_ = max(max_, dp[i] + dp_r[i])

print(max_)
