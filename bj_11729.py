n = int(input())

def hanoi(n, start, assist, end):
  if n == 1:
    print(start, end)
  else:
    hanoi(n - 1, start, end, assist)
    print(start, end)
    hanoi(n - 1, assist, start, end)

sum = 1
for _ in range(n - 1):
  sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)
