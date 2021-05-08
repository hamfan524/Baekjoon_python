t = int(input())
sum_case = []

for i in range(t):
  a ,b = list(map(int, input().split()))
  sum_case.append(a + b)

for i in range(t):
  print("Case #{}: {}".format(i + 1,sum_case[i]))