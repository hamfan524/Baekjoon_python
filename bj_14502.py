import sys, copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
max_num = 0

empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2

graph = []

for y in range(n):
    graph.append(list(map(int, input().split())))
    for x in range(m):
        if graph[y][x] == EMPTY:
            empty_list.append([y, x])
        if graph[y][x] == VIRUS:
            virus_list.append([y, x])
    
def bfs(g):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    global max_num

    q = deque()
    visit = [[0] * m for _ in range(n)]
    cnt = 0

    for v in virus_list:
        q.append(v)
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n \
                and visit[ny][nx] == 0 and g[ny][nx] == EMPTY:
                g[ny][nx] = VIRUS
                visit[ny][nx] = 1
                q.append([ny, nx])

    for i in range(n):
            cnt += g[i].count(EMPTY)
        
    if max_num < cnt:
            max_num = cnt

for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            graph[y1][x1] = WALL
            graph[y2][x2] = WALL
            graph[y3][x3] = WALL

            g = copy.deepcopy(graph)
            bfs(g)

            graph[y1][x1] = EMPTY
            graph[y2][x2] = EMPTY
            graph[y3][x3] = EMPTY

print(max_num)
