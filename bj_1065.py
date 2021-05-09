def sort(num):

  count = 0
  f = 0
  if len(str(num)) > 2:
    count += 99
    for i in range(100, num + 1):
      a = str(i)
      sum = 0
      for j in a:
        sum += int(j)
      if (sum / 3) == int(a[1]):
        f += 1
  else:
    count = num
  return count + f

n = int(input())
print(sort(n))
