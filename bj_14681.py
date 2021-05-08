x = int(input())
y = int(input())

print(1 if x > 0 and y > 0\
  else(2 if x < 0 and y > 0\
    else(3 if x < 0 and y < 0\
       else(4 if x > 0 and y < 0 else print("0이외의 숫자를 입력하시오")))))