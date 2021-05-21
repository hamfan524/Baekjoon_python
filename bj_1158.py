from collections import deque
n,k=map(int,input().split())
a=deque()
y=[]
blank = []
for i in range(n):
  a.append(i+1)
for i in range(n):
  blank.clear()
  if len(a) >=k:
    for j in range(k):
      b=a.popleft()
      if j==(k-1):
        y.append(b)
      else:
        a.append(b)    
  else:
    c=k%len(a)
    if  c==0:
      b=a.pop()
      y.append(b)
    else:
      c-=1
      for i in range(c + 1):
        t = a.popleft()
        blank.append(t)
      for i in range(c):
        a.append(blank[i])
      b = blank[c]
      y.append(b)
print('<', end="")
for i in y:
  if i != y[-1]:
    print(i, end=", ")
  else:
    print(i, end="")
print('>')
