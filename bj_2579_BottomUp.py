import sys
input = sys.stdin.readline

n = int(input())

stair = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
  if i == 0:
    dp[i] = stair[i]
  elif i == 1:
    dp[i] = stair[i-1] + stair[i]
  elif i == 2:
    dp[i] = max(stair[i-1] + stair[i], stair[i-2] + stair[i])
  else:
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n-1])