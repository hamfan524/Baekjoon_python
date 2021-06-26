import sys

input = sys.stdin.readline
inf = sys.maxsize

v, e = map(int, input().split())
dist = [[inf] * v for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = inf
for i in range(v):
    ans = min(ans, dist[i][i])

print(ans if ans != inf else -1)