import sys
input = sys.stdin.readline

dp = {
  0 : 1,
  1 : 1,
  2 : 2
}

def f(n):
  if n not in dp:
    dp[n] = n * f(n -1)
  return dp[n] 

def solve():
  n, m = map(int, input().split())
  result = f(m) // (f(m-n) * f(n))
  return print(result)

t = int(input())
for _ in range(t):
  solve()
