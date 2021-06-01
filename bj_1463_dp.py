import sys
input = sys.stdin.readline

dp = {
  1 : 0,
  2 : 1,
  3 : 1
}

n = int(input())

for i in range (4, 1000001):
  if i % 3 == 0 and i % 2 == 0:
    dp[i] = min(dp[i//3] + 1, dp[i//2] + 1, dp[i-1] + 1)
  elif i % 3 == 0:
    dp[i] = min(dp[i//3] + 1, dp[i-1] + 1) 
  elif i % 2 == 0:
    dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
  else:
    dp[i] = dp[i-1] + 1

print(dp[n])