s = list(input())
b = []
for i in range(ord('a'), ord('z') + 1):
  if chr(i) in s:
    b.append(s.index(chr(i)))
  else:
    b.append(-1) 

for i in b:
  print(i, end=" ")
