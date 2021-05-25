import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n)]

e = [list(map(int, input().split())) for _ in range(n)]
e.sort(key= lambda i:i[0])
eb = []

for i in range(n):
  eb.append(e[i][1])
for i in range(n):
  for j in range(i):
    if eb[i] > eb[j] and dp[i] < dp[j]:
      dp[i] = dp[j]
  dp[i] += 1

print(n - max(dp))