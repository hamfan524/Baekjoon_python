n = int(input())
a = []
b = []
k = 0
for i in range(0, n):
  a.append(input())
  b.append('YES')
for i in a:
  c = 0
  d = 0
  for j in i:
    if d > c:
     b[k] = 'NO'
     break
    elif j == '(':
      c += 1
    elif j == ')':
      d += 1
  if c != d:
    b[k] = 'NO'
  k += 1
for i in b:
  print(i) 