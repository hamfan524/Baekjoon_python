t = int(input())

for i in range(t):
  h, w, n = map(int, input().split())
  if n % h != 0:
    a = str(n % h)
    b = str(n // h + 1).zfill(2)
    if int(b) > w:
      a = str(int(a)+ 1)
      b = str(w - int(b))
  else:
    a = str(h)
    b = str(n // h).zfill(2)

  print(a, b ,sep='') 
