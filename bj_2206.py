from collections import deque

def bfs():
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque()
  q.append([0, 0, 1])
  visited[0][0][1] = 1
  while q:
    x, y, count = q.popleft()
    if x == n - 1 and y == m - 1:
      return visited[x][y][count]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if field[nx][ny] == 1 and count == 1:
          visited[nx][ny][0] = visited[x][y][1] + 1
          q.append([nx, ny, 0])

        elif field[nx][ny] == 0 and visited[nx][ny][count] == 0:
          visited[nx][ny][count] = visited[x][y][count] + 1
          q.append([nx, ny, count])

  return -1        
  
n, m = map(int, input().split())
field = [list(map(int, input())) for _ in range(n)]
visited = [[[0]* 2 for i in range(m)] for i in range(n)]

print(bfs())