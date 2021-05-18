from collections import deque

def bfs(x, y, x_end, y_end):
  dx = [1, 1, 2, 2, -1, -1, -2, -2]
  dy = [2, -2, 1, -1, 2, -2, 1, -1]

  q = deque()
  q.append([x, y])
  field[x][y] = 1
  while q:
    x, y = q.popleft()
    if x == x_end and y == y_end:
      return field[x][y] - 1
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if field[nx][ny] == 0:
          field[nx][ny] = field[x][y] + 1
          q.append([nx, ny])

t = int(input())

for _ in range(t):
  n = int(input())
  field = [[0] * n for _ in range(n)]
  x, y = map(int, input().split())
  x_end, y_end = map(int, input().split())
  if x == x_end and y == y_end:
    print(0)
    continue

  print(bfs(x, y, x_end, y_end))