n = int(input())
a = list(map(int, input().split()))
b = max(a)

for i in range(n):
  a[i] = a[i] / b * 100

ave = sum(a) / n
print(ave)