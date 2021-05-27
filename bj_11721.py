import sys
input = sys.stdin.readline

dp = {
  1 : 1,
  2 : 3
}

def f(n):
  if n not in dp:
    dp[n] = f(n-1) + (f(n-2)*2)
  return dp[n]

n = int(input())
print(f(n) % 10007)