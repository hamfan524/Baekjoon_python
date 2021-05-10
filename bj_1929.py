def prime(n):       #소수 구하는 함수
  if n <= 1:
    return False
  elif n == 2:
    return True
  else:
    for i in range(2 , int(n ** 0.5) + 1):
      if n % i == 0 :
        return False
      else:
        continue
    return True

m, n = map(int, input().split())
a = []

for i in range(m, n +1):
  if prime(i) == True:
    a.append(i)

for i in a:
  print(i)