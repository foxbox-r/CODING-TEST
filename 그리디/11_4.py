import sys
input = sys.stdin.readline

data = list(map(int,input().split()))

data.sort()

target = 1

for x in data:
    if target < x:
        break
    target += x
    # target 구하는 공식 =  (target - 1) + target + 1 = x

print(target)
