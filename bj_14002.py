import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
dp = [0 for _ in range(n)]
array = [[x] for x in s]

for i in range(n):
  for j in range(i):
    if s[i] > s[j] and dp[i] < dp[j]:
      array[i] = array[j] + [s[i]]
      dp[i] = dp[j]
  dp[i] += 1

length = 0
flag = 0
for i in range(n):
  if length < dp[i]:
    flag = i
    length = dp[i]

print(length)
print(*array[flag])