import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
  q = deque()
  q.append(x)
  visited[x] = 1
  cnt = 0
  while q:
    temp = q.popleft()
    for i in graph[temp]:
      if visited[i] == 0:
        visited[i] = 1
        cnt += 1
        q.append(i)
  return cnt

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  visited = [0 for _ in range(n+1)]
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  ans = 0
  for i in range(1, n+1):
    if visited[i] == 0:
      ans += bfs(i)
  print(ans)