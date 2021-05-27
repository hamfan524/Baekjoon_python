import sys
input = sys.stdin.readline

dp = {
  0 : 0,
  1 : 1,
  2 : 1
}

def bn(n):
  if n not in dp:
    dp[n] = bn(n-1) + bn(n-2)
  return dp[n]

n = int(input())
print(bn(n))