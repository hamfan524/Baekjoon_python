import sys

read = sys.stdin.readline

def dfs(x, y):
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
      field[nx][ny] = 0
      dfs(nx, ny)

t = int(read())


for _ in range(t):
  m, n, k = map(int,read().split())
  field = list([0] * m for _ in range(n))
  days = 0
  for _ in range(k):
    x, y = map(int, read().split())
    field[y][x] = 1
  for i in range(n):
    for j in range(m):
      if field[i][j] == 1:
        field[i][j] = 0
        dfs(i, j)
        days += 1
  
  print(days)