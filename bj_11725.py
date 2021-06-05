from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = {i : [] for i in range(1, n+1)}
parents = [0] * n

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
q.append(1)

while q:
  temp = q.popleft()
  for i in graph[temp]:
    if parents[temp-1] != i:
      parents[i-1] = temp
      q.append(i)

for i in parents[1:]:
  print(i)