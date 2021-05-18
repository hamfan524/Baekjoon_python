from collections import deque

def bfs():
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque()
  q.append([0, 0, 1])                
  visited[0][0][1] = 1             # 방문 리스트

  while q:
    x, y, count = q.popleft()
    if x == n - 1 and y == m - 1:           # 마지막 점에 도착 시
      return visited[x][y][count]           # 리턴

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if field[nx][ny] == 1 and count == 1:           # 벽을 만났지만 부술 수 있는 기회가 1번 있을 시
          visited[nx][ny][0] = visited[x][y][1] + 1       # 벽을 부수고 기회는 0, 방문리스트 1로 변경
          q.append([nx, ny, 0])                         # 벽 부술 기회가 0으로 q에 입력

        elif field[nx][ny] == 0 and visited[nx][ny][count] == 0:    # 벽이 아닌곳을 만났는데 아직 방문하지 않았을 시
          visited[nx][ny][count] = visited[x][y][count] + 1   
          q.append([nx, ny, count])

  return -1        
  
n, m = map(int, input().split())
field = [list(map(int, input())) for _ in range(n)]       # 맵을 리스트로 선언
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]     #방문하지 않은 장소를 3차배열로 벽을 부쉈을때와 안부쉈을때로 나눠서 선언

print(bfs())