import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def prim(start, weight):
    visit = [False] * (V + 1) 
    heap = [[weight, start]] 
    ans = 0 
    cnt = 0 
    while cnt < V: 
        k, v = heappop(heap)
        if visit[v]: continue 
        visit[v] = True
        ans += k 
        cnt += 1 
        for u, w in graph[v]: 
            heappush(heap, [w, u])
        
    return ans 

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

print(prim(1, 0))
