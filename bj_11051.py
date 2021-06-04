import sys
input = sys.stdin.readline

dp = {
  0 : 1,
  1 : 1,
  2 : 2
}

def f(n):
  if n not in dp:
    dp[n] = f(n-1) * n
  return dp[n]

n, k = map(int, input().split())
answer = f(n) // (f(k) * f(n-k))

print(answer % 10007)