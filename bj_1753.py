import sys
input = sys.stdin.readline
from heapq import heappush, heappop

inf = 100000000
V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
dp = [inf] * (V + 1)
heap = []

def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dijkstra(k)
for i in dp[1:]:
    print(i if i != inf else "INF")