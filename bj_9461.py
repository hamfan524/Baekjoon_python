import sys
read = sys.stdin.readline

dic = {
  1 : 1,
  2 : 1,
  3 : 1
}

def f(n):
  if n not in dic:
    dic[n] = f(n - 3) + f(n - 2)
  return dic[n]

t = int(read())
for _ in range(t):
  n = int(read())
  print(f(n))