arr = [0] * 30001
arr[1] = 0
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 1

n = int(input())

def check(n):
    count = 0

    if arr[n-1] != 0:
        count = arr[n-1]

    if n%5 == 0 and arr[n//5] != 0:
        count = min(count,arr[n//5])

    if n % 3 == 0 and arr[n // 3] != 0:
        count = min(count, arr[n // 3])

    if n%2 == 0 and arr[n//2] != 0:
        count = min(count,arr[n//2])
    return count + 1


for i in range(6,len(arr)):
    arr[i] = check(i)

print(arr[n])