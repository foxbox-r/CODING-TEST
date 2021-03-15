import sys
input = sys.stdin.readline

n,x = map(int,input().split())
arr = list(map(int,input().split()))

def first(arr,target,start,end):
    if start > end:
        return -1
    mid = (start + end) // 2

    if arr[mid] == target and (mid == 0 or arr[mid - 1] < target):
        return mid
    elif arr[mid] < target:
        return first(arr,target,mid + 1,end)
    else:
        return first(arr,target,start,mid - 1)


def last(arr, target, start, end):
    global n
    mid = (start + end) // 2
    if arr[mid] == target and (mid == n-1 or target < arr[mid + 1]):
        return mid
    elif arr[mid] > target:
        return last(arr, target, start, mid - 1)
    else:
        return last(arr, target, mid + 1, end)

def get_result(arr):
    f = first(arr,x,0,n-1)
    if f == -1:
        return -1
    l = last(arr,x,0,n-1)

    return l-f+1

result = get_result(arr)
print(result)