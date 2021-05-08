a = int(input())
b = int(input())
c = int(input())

number = a * b * c

str_number = str(number)

for i in range(10):
  print(str_number.count(str(i)))