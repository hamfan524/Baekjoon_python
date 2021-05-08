import sys
t = sys.stdin.readline().rstrip()

sum_case = []

for i in range(int(t)):
  a, b = list(map(int , sys.stdin.readline().split()))
  sum_case.append(a + b)

for i in range(int(t)):
  print(sum_case[i])