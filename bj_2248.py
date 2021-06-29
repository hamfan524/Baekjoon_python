import sys

input =sys.stdin.readline

N, L, K = map(int, input().split())
dp = [[0] * 32 for _ in range(32)]
for i in range(31):
    dp[0][i] = 1
for i in range(1, 32):
    dp[i][0] = dp[i-1][0]
    for j in range(1, 32):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
while N > 0:
    if K <= dp[N-1][L]:
        print('0', end="")
        N -= 1
    else:
        print('1', end="")
        K -= dp[N-1][L]
        N -= 1
        L -= 1
