import sys

input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())

#최단 경로를 담는 배열
dist = [[inf] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a-1][b-1] > c:
        dist[a-1][b-1] = c

for k in range(n):          #거치는 점
    for i in range(n):         #시작 점
        for j in range(n):        #끝 점
                # k를 거쳤을 때 더 적은 경로
            if i != j and dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in dist:
    for j in i:
        if j == inf:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()