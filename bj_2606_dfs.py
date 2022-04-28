import sys
input = sys.stdin.readline

def dfs(start, dic):
  visited.append(start)
  for i in dic[start]:
    if i not in visited:
      dfs(i, dic)
  return len(visited) - 1

dic = {}
visited = []

for i in range(int(input())):
  dic[i + 1] = set()

for _ in range(int(input())):
  a, b = map(int, input().split())
  dic[a].add(b)
  dic[b].add(a)

print(dfs(1,dic))