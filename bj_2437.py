n = int(input())
a = list(map(int, input().split()))

a.sort()

answer = 1

for i in a:       #더하는 수가 목표로 하는 수보다 크면 안된다.
  if answer < i:
    break
  answer += i

print(answer)  
