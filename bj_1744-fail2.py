import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

p_a = []
n_a = []


for i in a:
  if i <= 0:
    n_a.append(i)
  else:
    p_a.append(i)

p_a.sort(reverse = True)
n_a.sort()
answer = 0


while len(p_a) > 1:
  temp1 = p_a[0]
  temp2 = p_a[1]
  if temp1 * temp2 > temp1 + temp2:
    answer += temp1 * temp2
    p_a.pop(1)
    p_a.pop(0)
  elif temp1 * temp2 < temp1 + temp2:
    answer += temp1 
    p_a.pop(0)
  if len(p_a) == 1:
    answer += p_a[0]
    break

while len(n_a) > 1:
  temp1 = n_a[0]
  temp2 = n_a[1]
  if temp1 * temp2 > temp1 + temp2:
    answer += temp1 * temp2
    n_a.pop(1)
    n_a.pop(0)
  elif temp1 * temp2 < temp1 + temp2:
    answer += temp1 
    n_a.pop(0)
  if len(n_a) == 1:
    answer += n_a[0]
    break

print(answer)

##..while문에 if문 때려박아서 시간 초과 ㅠ