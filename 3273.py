import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split())); numbers.sort()
x = int(input())

left, right = 0, n-1
count = 0

while left < right:
    tmp = numbers[left] + numbers[right]
    if tmp > x:
        right -= 1
    elif tmp < x:
        left += 1
    else:
        left += 1
        right -= 1
        count += 1
print(count)