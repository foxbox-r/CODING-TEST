n,m = map(int,input().split())
inf = 999999
money = []
arr = [inf] * (10001)

for _ in range(n):
    money.append(int(input()))

arr[0] = 0
for _m in money:
    arr[_m] = 1

for i in range(min(money),m+1):
    for _m in money:
        if i-_m >= 0:
            arr[i] = min(arr[i],arr[i-_m]+1)

print(arr[m] if arr[m] != inf else -1)