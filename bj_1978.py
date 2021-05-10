n = int(input())

num = map(int, input().split())

for i in num:
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        n -= 1
        break
  else:
    n -= 1
print(n)