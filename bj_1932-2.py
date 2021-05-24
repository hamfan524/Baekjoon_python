import sys
read = sys.stdin.readline

n = int(read())
pyramid = []
max_list = [[] for _ in range(n)]

for _ in range(n):
    pyramid.append(list(map(int, read().split())))

#역순으로 하위 항목을 모두 더한 최댓값을 저장
for i in range(n - 1, -1, -1):
    for j in range(len(pyramid[i])):
        if i == n - 1:
            max_list[i].append(pyramid[i][j])
        else:
            max_list[i].append(pyramid[i][j] + max(max_list[i+1][j], max_list[i+1][j+1]))

print(max_list[0][0])