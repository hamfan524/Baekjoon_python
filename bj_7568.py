import sys
input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
    w, h = map(int, input().split())
    p.append([w, h])

for i in p:
    rank = 1
    for j in p:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")