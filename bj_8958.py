n = int(input())
b = [] 
for i in range(n):
  a = list(map(str, input()))
  sum_a = 0
  cnt = 1
  for j in range(len(a)):
    if a[j] == "O":
      sum_a += cnt
      cnt += 1
    else:
      cnt = 1
  b.append(sum_a)
for j in range(n):
  print(b[j])
