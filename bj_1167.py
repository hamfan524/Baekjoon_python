import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
  a = list(map(int, input().split()))
  for i in range(1, len(a) -2, 2):
    graph[a[0]].append([a[i], a[i + 1]])
 
def bfs(start):
  visit = [-1] * (v + 1)
  q = deque()
  q.append(start)
  visit[start] = 0
  max_ = [0, 0]

  while q:
    temp = q.popleft()
    for i, j in graph[temp]:
      if visit[i] == -1:
        visit[i] = visit[temp] + j
        q.append(i)
        if max_[0] < visit[i]:
          max_ = visit[i], i

  return max_

dis, node = bfs(1)
dis, node = bfs(node)
print(dis) 