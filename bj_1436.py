import sys
input = sys.stdin.readline

n = int(input())
dn = "666"
i = 666
while True:
    if n == 1 and dn in str(i):
        print(i)
        break
    if n != 1 and dn in str(i):
        n -= 1
    i += 1