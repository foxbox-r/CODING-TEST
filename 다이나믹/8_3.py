n = int(input())
arr = [0] * (n+1)

value = [0] + list(map(int,input().split()))

arr[1] = value[1]
arr[2] = max(value[1],value[2])
for i in range(2,len(arr)):
    arr[i] = max(arr[i-1],arr[i-2]+value[i])

print(arr[n])
