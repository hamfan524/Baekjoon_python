n = int(input())
s = []

for i in range(n):
  start, finish = map(int, input().split())
  s.append([start, finish])

s = sorted(s, lambda s : s[0])
s = sorted(s, lambda s : s[1])
last = 0
cnt = 0

for i, j in s:
  if i >= last:
    cnt += 1
    last = j

print(cnt)