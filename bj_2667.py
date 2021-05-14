import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())
matrix = [list(map(int, list(read()))) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
  matrix[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if matrix[nx][ny] == 1:
        cnt = dfs(nx, ny, cnt + 1)
  return cnt

ans = []

for i in range(n):
  for j in range(n):
    if matrix[i][j] == 1:
      ans.append(dfs(i, j, 1))

print(len(ans))
for n in sorted(ans):
  print(n)