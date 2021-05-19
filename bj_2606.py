from collections import deque
import sys
read = sys.stdin.readline

def bfs(start, dic):
  q = deque()
  q.append(start)

  while q:
    start = q.popleft()
    for i in dic[start]:
      if i not in visited:
        visited.append(i)
        q.append(i)

  return len(visited) - 1

dic = {}
visited = []

for i in range(int(read())):
  dic[i + 1] = set()
for _ in range(int(read())):
  a, b = map(int, read().split())
  dic[a].add(b)
  dic[b].add(a)


print(bfs(1, dic))
