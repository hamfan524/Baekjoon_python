n = int(input())
d = [0]*1516

for i in range(2,n+1):
    if i%2 == 0:
        d[i] = (d[i-1] * 2 + 1) % 1000000007
    else:
        d[i] = (d[i-1] * 2 - 1) % 1000000007
print(d[n])