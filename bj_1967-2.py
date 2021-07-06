import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v - 1):
    parent, node, w = map(int, input().split())
    graph[parent].append([node, w])
    graph[node].append([parent, w])

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dp = [inf for _ in range(v + 1)]
    dp[start] = 0

    while heap:
        w, n = heappop(heap)
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
    
    return dp

d = dijkstra(1)
f_node = d.index(max(d[1:]))
d_ = dijkstra(f_node)
ans = max(d_[1:])
print(ans)