max_num = 0
count = 0

for i in range(1,10):
  a = int(input())
  if max_num < a:
    max_num = a
    count = i

print(max_num)
print(count)