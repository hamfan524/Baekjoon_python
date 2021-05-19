from collections import deque
import sys
read = lambda : sys.stdin.readline().strip()

def bfs(x, y, cnt):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  q = deque()
  q.append([x, y])
  field[x][y] = 0
  while q:
    a, b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < n and 0 <= ny < n and field[nx][ny] == 1:  
        field[nx][ny] = 0
        q.append([nx, ny])
        cnt += 1
  return cnt

n = int(read())

field = [list(map(int, list(read()))) for _ in range(n)]  
answer = []

for i in range(n):
  for j in range(n):
    if field[i][j] == 1:

      answer.append(bfs(i, j, 1))

print(len(answer))
answer.sort()
for i in answer:
  print(i) 