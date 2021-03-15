import sys
from collections import deque
input = sys.stdin.readline

arr = list(map(int,input().split()))
arr.sort()
arr = deque(arr)

result = 0
p_count = 0
now_num = 0

while arr:
    p_count += 1
    now_num = arr.popleft()
    if(p_count == now_num):
        result += 1
        p_count = 0

print(result)

