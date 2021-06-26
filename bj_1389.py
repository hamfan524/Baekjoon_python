import sys

input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())

graph =[[inf] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
sum = [0] * n
ans = inf
for i in range(n):
    for j in range(n):
        sum[i] += graph[i][j]
    if ans > sum[i]:
        ans = sum[i]
        result = i
        
print(result + 1)