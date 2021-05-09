def solve(a):
  sum_a = 0
  for i in range(len(a)):
    sum_a += a[i]
  return sum_a

a = list(map(int, input().split()))
