w = input().upper()
set_w = list(set(w))

a = []

for i in set_w:
  cnt = w.count(i)
  a.append(cnt)

if a.count(max(a)) > 1 :
  print("?")
else:
  max_index = a.index(max(a))
  print(set_w[max_index])