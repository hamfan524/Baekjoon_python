import sys

t = int(input())

for i in range(t):
  people = []
  cnt = 1
  n = int(input())

  for j in range(n):
    paper, interview = map(int, sys.stdin.readline().split())
    people.append([paper, interview])
  
  people.sort()
  max = people[0][1]

  for j in range(1, n):
    if max > people[j][1]:
      cnt += 1
      max = people[j][1]
  
  print(cnt)
