import sys
input = sys.stdin.readline
result = []

def showArr(arr):
    _m = -1
    for i in range(len(arr)):
        print(arr[i])
        _m = max(_m,arr[i][len(arr[0])-1])
    print(_m)


def check(arr,row,col,value,height):
    top,mid,bottom = value,value,value
    if row-1 != -1:
        top += arr[row-1][col-1]
    mid += arr[row][col-1]
    if row+1 != height:
        bottom += arr[row+1][col-1]
    arr[row][col] = max(top,mid,bottom)

for _ in range(int(input())):
    row,col = map(int,input().split())
    _arr = list(map(int,input().split()))
    arr = []

    for i in range(row):
        arr.append(_arr[i*col:i*col+col])

    _arr = [([arr[i][0]]+([0]*(col-1))) for i in range(row)]

    for i in range(1,col):
        for j in range(0,row):
            check(_arr,j,i,arr[j][i],row)

    showArr(_arr)



# 1
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7