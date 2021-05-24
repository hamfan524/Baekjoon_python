import sys
read = sys.stdin.readline

n = int(read())

pyramid = [list(map(int, read().split())) for _ in range(n)]

for i in range(1, n):
  for j in range(len(pyramid[i])):
    if j == 0:
      pyramid[i][j] += pyramid[i-1][j]
    elif j == i:
      pyramid[i][j] += pyramid[i-1][j-1]
    else:
      pyramid[i][j] += max(pyramid[i-1][j], pyramid[i-1][j-1])

print(max(pyramid[n-1]))