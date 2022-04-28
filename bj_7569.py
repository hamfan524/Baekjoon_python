import sys
from collections import deque
input = sys.stdin.readline

def bfs(m, n, h, box):
  dx = [1, -1, 0, 0, 0, 0]
  dy = [0, 0, 1, -1, 0, 0]
  dz = [0, 0, 0, 0, 1, -1]

  days = -1

  while q:
    days += 1
    for _ in range(len(q)):
      x, y, z = q.popleft()
      for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
          box[nx][ny][nz] = 1
          q.append([nx, ny, nz])
  
  for i in box:
    for j in i:
      if 0 in j:
        return -1
  return days


m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if box[i][j][k] == 1:
        q.append([i, j, k])

print(bfs(m, n, h, box))