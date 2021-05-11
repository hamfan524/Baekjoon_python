mon = [500 , 100, 50, 10, 5, 1]

n = int(input())
a = 1000 - n

cnt = 0

for i in mon:
  if a >= i and a > 0:
    cnt += (a // i)
    a %= i  
  elif a <= 0:
    break

print(cnt)

  