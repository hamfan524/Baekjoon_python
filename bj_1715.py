import heapq

n = int(input())

card = list(int(input()) for _ in range(n))
heapq.heapify(card)

answer = 0
while len(card) > 1:
  temp1 = heapq.heappop(card)
  temp2 = heapq.heappop(card)
  answer += temp1 + temp2
  heapq.heappush(card, temp1 + temp2)

print(answer)
