import sys
input = sys.stdin.readline

dp = {
  0 : 0,
  1 : 0,
  2 : 3
}
def f(n):
  if n not in dp:
    if n % 2 == 1:
      dp[n] = 0
    else:
      dp[n] = f(n - 2) + 2
      for i in range(2, n, 2):
        dp[n] += f(n - i) * 2
  return dp[n]   

n = int(input())
print(f(n))