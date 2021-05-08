a = int(input())
b = a
count = 0
while True:
  if a < 10:
    a = (a * 10) + a
  else:
    a = int(str(a % 10) + str(((a // 10) + (a % 10))% 10))  
  count += 1
  if b == a:
    break

print(count)
