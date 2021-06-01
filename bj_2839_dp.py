import sys
input = sys.stdin.readline

n = int(input())

dp = {
  3 : 1,
  4 : -1,
  5 : 1,
  6 : 2,
  7 : -1,
  8 : 2,
  9 : 3,
  10 : 2,
  11 : 3,
  12 : 4
}

for i in range(13, 5001):
  dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
print(dp[n])