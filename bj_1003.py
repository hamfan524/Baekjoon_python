import sys
read = sys.stdin.readline

dp ={
  0 : 0,
  1 : 1,
  2 : 1
}

def f(n):
  if n not in dp:
    dp[n] = f(n - 1) + f(n - 2)
  return dp[n]

t = int(read())
for _ in range(t):
  num = int(read())
  if not num:
    print('1 0')
  else:
    f(num)
    print(dp[num - 1], dp[num])