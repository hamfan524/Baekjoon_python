import sys
from heapq import heappop, heappush
import copy

input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dp = [inf] * (n + 1)
heap = []
city = [[] for _ in range(n + 1)]

def dijkstra(start):
    heappush(heap, [0, start])
    dp[start] = 0
    city.append(start)
    while heap:
        w, n = heappop(heap)
        city[n].append(n)
        if n == end:
            break
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
                city[n_n] = copy.deepcopy(city[n])

for _ in range(m):
    d, a, v = map(int, input().split())
    graph[d].append([a, v])

start, end = map(int , input().split())

dijkstra(start)

print(dp[end])
print(len(city[end]))
print(*city[end])