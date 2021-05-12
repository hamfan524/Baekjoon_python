import heapq

n = int(input())

a = []
for _ in range(n):
  heapq.heappush(a, int(input()))

answer = 0
while len(a) > 1:
  temp1 = heapq.heappop(a)
  temp2 = heapq.heappop(a)
  if temp1 * temp2 > temp1 + temp2:
    answer += temp1 * temp2
  elif temp1 * temp2 < temp1 + temp2:
    answer += temp1
    heapq.heappush(a, temp2)

if len(a) == 1:
  temp1 = heapq.heappop(a)
  answer += temp1

print(answer)

#ㅠㅠ 힙큐 특징인 작은 수부터 찾다보니 반례가 너무 많아 실패

