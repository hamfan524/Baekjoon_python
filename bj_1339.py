n = int(input())

words = []

for i in range(n):
  words.append(input())

dict = {}

for word in words:
  k = len(word) - 1
  for s in word:
    if s in dict:
      dict[s] += pow(10, k)
    else:
      dict[s] = pow(10, k)
    k -= 1

numbers = []

for value in dict.values():
  numbers.append(value)

numbers.sort(reverse = True)

result, t = 0 , 9

for i in range(len(numbers)):
  result += numbers[i] * t
  t -= 1

print(result)