import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

cnt = 1

def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    heap = []
    dp = [[inf] * n for _ in range(n)]
    dp[0][0] = maze[0][0]
    visit = [[0] * n for _ in range(n)]
    visit[0][0] = 1

    heappush(heap, [maze[0][0], 0, 0])
    while heap:
        c, x, y = heappop(heap)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + maze[nx][ny])
                heappush(heap, [dp[nx][ny], nx, ny])
                visit[nx][ny] = 1
    return dp[n-1][n-1]

while True:
    n = int(input())
    if n == 0:
        break
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    ans = dijkstra()
    print(f"Problem {cnt}: {ans}")
    cnt += 1