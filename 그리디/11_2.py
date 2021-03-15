import sys

input = sys.stdin.readline

string = input()

result = int(string[0])

for i in range(1,len(string)-1):
    cur = int(string[i])
    if result == 0 or  result == 1 or cur == 0 or cur == 1:
        result += cur
    else:
        result *= cur
print(result)