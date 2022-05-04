import sys

input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())

#최단 경로를 담는 배열
graph = [[inf] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for k in range(n):          #거치는 점
    for i in range(n):         #시작 점
        for j in range(n):        #끝 점
                # k를 거쳤을 때 더 적은 경로
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in graph:
    for j in i:
        if j == inf:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()