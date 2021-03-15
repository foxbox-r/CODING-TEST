import sys
input = sys.stdin.readline

string = input()

resultArr = [0,0]

prevStatus = 9999

for i in range(0,len(string)-1):
    curStatus = int(string[i])
    if curStatus != prevStatus:
        resultArr[curStatus] += 1
        prevStatus = curStatus

print(min(resultArr[0],resultArr[1]))
