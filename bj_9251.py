temp1 = input()
temp2 = input()

t1_len = len(temp1)
t2_len = len(temp2)

dp = [[0] * (t2_len + 1) for _ in range(t1_len + 1)]
for i in range(t1_len):
  for j in range(t2_len):
    if temp1[i] == temp2[j]:
      dp[i+1][j+1] = dp[i][j] + 1
    else:
      dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[t1_len][t2_len])

