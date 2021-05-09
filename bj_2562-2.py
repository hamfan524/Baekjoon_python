a = []
max_num = 0
for i in range(9):
  a.append(int(input()))
  if max_num < a[i]:
    max_num = a[i]
b = int(a.index(max_num)) + 1
print(max_num)
print(b)   

