import sys
input = sys.stdin.readline

def solution(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i+1][0:len(numbers[i])]:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input().strip())
    numbers.sort()
    solution(numbers)
