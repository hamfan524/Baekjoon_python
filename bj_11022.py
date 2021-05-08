t = int(input())
num1 = []
num2 = []
sum_case = []

for i in range(t):
  a ,b = list(map(int, input().split()))
  num1.append(a)
  num2.append(b)
  sum_case.append(a + b)
for i in range(t):
  print("Case #{}: {} + {} = {}".format(i + 1, num1[i], num2[i], sum_case[i]))