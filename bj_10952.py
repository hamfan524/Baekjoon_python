sum_list = []

while True:
  try:
    a, b = list(map(int, input().split()))
    sum_list.append(a + b)
  except:
    break

i = 0
while True:
  try:
    print(sum_list[i])
    i += 1
  except:
    break
