import sys
from collections import deque
read = sys.stdin.readline

def bfs(m, n, box):

  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]

  days = -1

  while ripe:
    days += 1
    for _ in range(len(ripe)):
      x, y = ripe.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
          box[nx][ny] = 1
          ripe.append([nx, ny])
  
  for b in box:
    if 0 in b:
      return -1
  return days

m, n = map(int, read().split())
box, ripe = [], deque()

for i in range(n):
  row = list(map(int, read().split()))
  box.append(row)
  for j in range(m):
    if row[j] == 1:
      ripe.append([i, j])
 

print(bfs(m, n, box))
          
