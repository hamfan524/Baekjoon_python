n = int(input())
a = list(map(int,input().split()))

b = []
c = []
b = sorted(a)
sum_n = 0

for i in b:
  sum_n += i
  c.append(sum_n)

print(sum(c))
