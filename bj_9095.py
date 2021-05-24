import sys
input = sys.stdin.readline

dp = {
  1 : 1,
  2 : 2,
  3 : 4
}

def f(n):
  if n not in dp: 
    dp[n] = f(n-1) + f(n-2) + f(n-3)
  return dp[n]

t = int(input())

for _ in range(t):
  n = int(input())
  print(f(n))
