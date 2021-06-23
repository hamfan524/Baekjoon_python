import sys
input = sys.stdin.readline

t = int(input().rstrip())
sum_case = []

for i in range(t):
  a, b = map(int , input().split())
  sum_case.append(a + b)

for i in range(t):
  print(sum_case[i])