import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

def binarySearch(arr,start,end):
    if start > end:
        return -1
    midIndex = (start + end) // 2

    if arr[midIndex] == midIndex:
        return midIndex
    elif arr[midIndex] > midIndex:
        return binarySearch(arr,start,midIndex-1)
    else:
        return binarySearch(arr,midIndex+1,end)

print(binarySearch(arr,0,n-1))