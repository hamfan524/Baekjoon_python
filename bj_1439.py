s = list(input())
a, b = 0, 0

if s[0] == '0':
  a = 1
else:
  b = 1

for i in range(1, len(s)):
  if s[i] != s[i - 1]:
    if s[i] == '0':
      a += 1
    else:
      b += 1

if a >= b:
  print(b)
else:
  print(a)
