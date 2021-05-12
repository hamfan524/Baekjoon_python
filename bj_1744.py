import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

p_a = []
n_a = []

answer = 0

for i in a:
  if i <= 0:
    n_a.append(i)
  elif i == 1:
    answer += i
  else:
    p_a.append(i)

n_a.sort()
p_a.sort(reverse = True)

for i in range(0, len(n_a), 2):
  if i + 1 < len(n_a):
    answer += n_a[i] * n_a[i + 1]
  else:
    answer += n_a[i]

for i in range(0, len(p_a), 2):
  if i + 1 < len(p_a):
    answer += p_a[i] * p_a[i + 1]
  else:
    answer += p_a[i]

print(answer)