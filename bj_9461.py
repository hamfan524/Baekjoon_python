import sys
input = sys.stdin.readline

dic = {
  1 : 1,
  2 : 1,
  3 : 1
}

def f(n):
  if n not in dic:
    dic[n] = f(n - 3) + f(n - 2)
  return dic[n]

t = int(input())
for _ in range(t):
  n = int(input())
  print(f(n))