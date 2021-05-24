import sys
read = sys.stdin.readline

n = int(read())
house = [list(map(int, read().split())) for _ in range(n)]

for i in range(1, n):
  house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
  house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
  house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]

print(min(house[-1][0],house[-1][1],house[-1][2]))
