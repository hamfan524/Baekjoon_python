import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
           if graph[i][k] and graph[k][j]:
               graph[i][k] = 1

res = 0
for i in range(n):
    t = 0
    for j in range(n):
        t += graph[i][j] + graph[j][i]
    if t == n - 1:
        res += 1
print(res)