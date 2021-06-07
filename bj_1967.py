import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v-1):
  a = list(map(int, input().split()))
  graph[a[0]].append([a[1], a[2]])
  graph[a[1]].append([a[0], a[2]])
  
def bfs(start):
  q = deque()
  q.append(start)
  visit = [-1] * (v + 1)
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
