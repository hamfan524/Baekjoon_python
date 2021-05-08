num1 = int(input())
num2 = int(input())

digit1 = num1 * ((num2 %  10) // 1)
digit2 = num1 * ((num2 % 100) // 10)
digit3 = num1 * ((num2 % 1000) // 100)
result = (digit3 * 100) + (digit2 * 10) + digit1

print(digit1)
print(digit2)
print(digit3)
print(result)