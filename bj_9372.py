import sys
input = sys.stdin.readline
def solve():
  n, m = map(int, input().split())
  for _ in range(m):
    a, b = map(int, input().split())
  print(n-1)
  
for _ in range(int(input())):
  solve()