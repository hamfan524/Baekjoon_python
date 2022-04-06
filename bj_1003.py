import sys
input = sys.stdin.readline

dp ={
  0 : 0,
  1 : 1
}

def fibo(n):
  if n not in dp:
    dp[n] = fibo(n - 1) + fibo(n - 2)
  return dp[n]

t = int(input())
for _ in range(t):
  num = int(input())
  if not num:
    print('1 0')
  else:
    fibo(num)
    print(dp[num - 1], dp[num])