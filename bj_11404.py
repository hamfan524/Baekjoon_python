import sys

input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())
graph = [[inf] * n for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    print(*graph[i])