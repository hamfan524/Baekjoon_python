import sys
input = sys.stdin.readline

n = int(input())

sequence = list(map(int, input().split()))
dp = [sequence[0]]

for i in range(n-1):
  dp.append(max(dp[i] + sequence[i+1], sequence[i+1]))

print(max(dp))

