import sys
input = sys.stdin.readline

dp = {
  1 : 1,
  2 : 2,
  3 : 4,
  4 : 7
}
def f(n):
  if n not in dp:
    dp[n] = f(n-3) + f(n-2) + f(n-1)
  return dp[n]

def solve():
  n = int(input())
  print(f(n))

t = int(input())
for _ in range(t):
  solve()