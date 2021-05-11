n = int(input())
a= []

for i in range(n):
  a.append(int(input()))

a.sort(reverse = True)

for i in range(len(a)):
  a[i] = a[i] * (i + 1)

print(max(a))