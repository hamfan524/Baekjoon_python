import sys
from collections import deque
read = sys.stdin.readline

def bfs(m, n, h, box):
  dx = [1, -1, 0, 0, 0, 0]
  dy = [0, 0, 1, -1, 0, 0]
  dz = [0, 0, 0, 0, 1, -1]

  days = -1

  while ripe:
    days += 1
    for _ in range(len(ripe)):
      x, y, z = ripe.popleft()
      for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
          box[nx][ny][nz] = 1
          ripe.append([nx, ny, nz])
  
  for i in box:
    for j in i:
      if 0 in j:
        return -1
  return days


m, n, h = map(int, read().split())
box = [[list(map(int, read().split())) for _ in range(n)] for _ in range(h)]
ripe = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if box[i][j][k] == 1:
        ripe.append([i, j, k])


print(bfs(m, n, h, box))