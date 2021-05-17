t = int(input())
output = []
for i in range(t):
  Pstr = input() 
  output.append('YES')
  stack = []

  for j in Pstr:
    if j == '(':
      stack.append(j)
    else:
      if len(stack) == 0:
        output[i] = 'NO'
        break
      else:
        stack.pop()
        
  if len(stack) != 0:
    output[i] = 'NO'

for i in output:
  print(i)