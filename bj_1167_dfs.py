import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

v = int(input())
graph = [[] for _ in range(v + 1)]
visit1 = [-1] * (v + 1)
visit2 = [-1] * (v + 1)

for _ in range(v):
  a = list(map(int, input().split()))
  for i in range(1, len(a) -2, 2):
    graph[a[0]].append([a[i], a[i + 1]])

def dfs(start, visited):
    for i, j in graph[start]:
        if visited[i] == -1:
            visited[i] = visited[start] + j
            dfs(i, visited)
           
visit1[1] = 0
dfs(1, visit1)

temp = max(visit1)
index = visit1.index(temp)

visit2[index] = 0
dfs(index, visit2)

print(max(visit2))


