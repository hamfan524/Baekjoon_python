import sys
write = sys.stdout.write

def star(x, y, size):
  if size == 1:
    field[x][y] = '*'
    return
  for i in range(3):
    for j in range(3):
      if i != 1 or j != 1:
        star(x + size // 3 * i, y + size // 3 * j, size // 3)

n = int(input())
field = [[' '] * n for i in range(n)]
star(0, 0, n)

for i in field:
  for j in i:
    write(j)
  write('\n')
