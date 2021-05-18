from collections import deque
import sys

read = sys.stdin.readline

def bfs(start):
  visited[start] = 1
  q = deque()
  q.append(start)
  while q:
    a = q.popleft()
    for i in graph[a]:
      if visited[i] == 0:
        visited[i] = -visited[a]
        q.append(i)
      else:
        if visited[i] == visited[a]:
          return False
  return True

t = int(read())

for i in range(t):
  v, e = map(int, read().split())
  graph = [[] for _ in range(v + 1)]
  visited = [0] * (v + 1)
  check = True
  for j in range(e):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
  for k in range(1, v + 1):
    if visited[k] == 0:
      if not bfs(k):
        check = False
        break
  print('YES' if check == True else 'NO')