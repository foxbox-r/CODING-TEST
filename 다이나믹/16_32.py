import sys
input = sys.stdin.readline

arr = []
n = int(input())

def set_max(arr,f,j):
    arr[f][j] += max(arr[f+1][j],arr[f+1][j+1])

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n-1):
    f = n-i-2
    for j in range(len(arr[f])):
        set_max(arr,f,j)

# print(arr)

print(arr[0][0])