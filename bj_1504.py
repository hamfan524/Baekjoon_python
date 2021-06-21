import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp_1 = [inf] * (n + 1)
dp_2 = [inf] * (n + 1)
dp_3 = [inf] * (n + 1)

def dijkstra(start, dp):
    heap = []
    heappush(heap, [0, start])
    dp[start] = 0
    while heap:
        w, n = heappop(heap)
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())
dijkstra(1, dp_1)
dijkstra(v1, dp_2)
dijkstra(v2, dp_3)

min_ = min(dp_1[v1] + dp_2[v2] + dp_3[n], dp_1[v2] + dp_2[n] + dp_3[v1])
if min_ >= inf:
    print(-1)
else:
    print(min_)