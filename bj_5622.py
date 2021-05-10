alph=['1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','0']
a = input()
sum = 0
for i in a:
  for j in alph:
    if i in j:
      sum += alph.index(j) + 2
      break
print(sum)