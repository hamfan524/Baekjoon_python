import sys
input = sys.stdin.readline

n = int(input())

stair = [0]
for _ in range(n):
  stair.append(int(input()))

dp = {
  0 : 0,
  1 : stair[1]
}

if n >= 2:
  dp[2] = stair[1] + stair[2]
elif n >= 3:
  dp[3] = max(dp[0] + dp[2] + stair[3], dp[1] + stair[3])
  
def find(n):
  if n not in dp:
    dp[n] = max(find(n-2) + stair[n], find(n-3) + stair[n-1] + stair[n])
  return dp[n]

print(find(n))