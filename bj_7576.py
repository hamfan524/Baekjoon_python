import sys
from collections import deque
input = sys.stdin.readline

def bfs(m, n, box):

  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]

  days = -1

  while q:
    days += 1
    for _ in range(len(q)):
      x, y = q.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
          box[nx][ny] = 1
          q.append([nx, ny])
  
  for b in box:
    if 0 in b:
      return -1
  return days

m, n = map(int, input().split())
box, q = [], deque()

for i in range(n):
  row = list(map(int, input().split()))
  box.append(row)
  for j in range(m):
    if row[j] == 1:
      q.append([i, j])
 

print(bfs(m, n, box))
          
