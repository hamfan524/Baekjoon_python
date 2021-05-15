import sys
from collections import deque

read = sys.stdin.readline

def bfs(x, y, q):
  q.append([x, y])
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  
  while q:
    a, b = q.popleft()
    for i in range(4):      #상하좌우 확인
      nx = a + dx[i] 
      ny = b + dy[i]
      if 0 <= nx < n and 0 <= ny < m  and field[nx][ny] == 1:
        field[nx][ny] = 0       #인접해 있는 1 다 0으로 변경
        q.append([nx, ny])


t = int(read())
q = deque()

for _ in range(t):
  m, n, k = map(int, read().split())
  field = [[0] * m for _ in range(n)]
  result = 0
  for _ in range(k):        #배추 위치 입력
    x, y = map(int, read().split())
    field[y][x] = 1
  for i in range(n):
    for j in range(m):
      if field[i][j] == 1:
        field[i][j] = 0    
        bfs(i, j, q)
        result += 1         #영역 수 추가
  print(result)