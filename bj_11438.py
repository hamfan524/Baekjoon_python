import sys
from math import log2
from collections import deque

input = sys.stdin.readline

n = int(input())
logN = int(log2(n) + 1)
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  p, c = map(int, input().split())
  tree[c].append(p)
  tree[p].append(c)

p_list = [0 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]

p_check = [True for _ in range(n+1)]

q = deque()
q.append(1)
while q:
  p = q.popleft()
  p_check[p] = False
  for i in tree[p]:
    if p_check[i]:
      q.append(i)
      p_list[i] = p
      depth[i] = depth[p] +1

dp = [[0 for _ in range(logN)] for _ in range(n + 1)]

for i in range(n+1):
  dp[i][0] = p_list[i]

for j in range(1, logN):
  for i in range(1, n+1):
    dp[i][j] = dp[dp[i][j-1]][j-1]


m= int(input())
for _ in range(m):
  a, b = map(int, input().split())
  if depth[a] > depth[b]:
    a, b = b, a
  
  dif = depth[b] - depth[a]

  for i in range(logN):
    if dif & 1 << i:
      b = dp[b][i]
  
  if a == b:
    print(a)
    continue

  for i in range(logN-1, -1, -1):
    if dp[a][i] != dp[b][i]:
      a = dp[a][i]
      b = dp[b][i]
  
  print(dp[b][0])
