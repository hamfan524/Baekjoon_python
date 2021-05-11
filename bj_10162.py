n = int(input())

a = [300, 60, 10]
b = []
if n % 10 != 0:
  print(-1)
else:
  for i in a:
    if n >= i:
      b.append(n // i)
      n = n % i
    else:
      b.append(0)
  for i in b:
    print(i, end=' ')
