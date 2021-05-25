import sys
input = sys.stdin.readline

dp = {
  1 : 1,
  2 : 2,
  3 : 3
}

def f(n):
  if n not in dp:
    dp[n] = f(n-2) + f(n-1)
  return dp[n]

n = int(input())

print(f(n) % 10007)
