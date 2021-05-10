n = int(input())

a = 1
b = 6
count = 1
while n > a:
  count += 1
  a += b
  b += 6

print(count)