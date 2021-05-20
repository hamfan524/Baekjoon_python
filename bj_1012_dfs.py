import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
 
  field[x][y] = 0

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
      dfs(nx, ny) 

t = int(read())

for _ in range(t):
  m, n, k = map(int, read().split())
  field = [[0] * m for _ in range(n)]
  result = 0
  for _ in range(k):
    a, b = map(int, read().split())
    field[b][a] = 1

  for i in range(n):
    for j in range(m):
      if field[i][j] == 1:
        dfs(i, j)
        result += 1

  print(result)