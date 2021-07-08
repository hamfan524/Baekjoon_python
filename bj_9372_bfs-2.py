import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, g, v):
    q = deque()
    q.append(start)
    v[start] = 1
    cnt = 0
    while q:
        temp = q.popleft()
        for i in g[temp]:
            if v[i] == 0:
                v[i] = 1
                cnt += 1
                q.append(i)
    return cnt
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visit = [0 for _ in range(n + 1)]

    ans = bfs(1, graph, visit)
    print(ans)

t = int(input())
for _ in range(t):
    solution()