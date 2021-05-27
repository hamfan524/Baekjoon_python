import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = []

for _ in range(n):
  t_, p_ = map(int, input().split())
  t.append(t_)
  p.append(p_)
  dp.append(p_)
dp.append(0)

for i in range(n-1, -1, -1):
  if t[i] + i > n:
    dp[i] = dp[i+1]
  else:
    dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

print(max(dp))
  