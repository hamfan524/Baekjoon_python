import sys
input = sys.stdin.readline

dp = {
  0 : 0,
  1 : 1
}

def fibo(n):
  if n not in dp:
    dp[n] = fibo(n-2) + fibo(n-1)
  return dp[n]

n = int(input())
print(fibo(n))