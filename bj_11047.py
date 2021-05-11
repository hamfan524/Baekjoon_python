n, k = map(int, input().split())

money = []
count = 0

for i in range(n):
  m = int(input())
  money.append(m)

for i in reversed(money):
  if i <= k:
    count += k // i
    k = k % i

print(count)
