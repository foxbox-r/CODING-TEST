import sys
input = sys.stdin.readline

arr = []

string = list(input())
string.pop()
string.sort()

sumNum = 0
sumString = ""

def charToInt(c):
    global sumNum,sumString

    num = ord(c)-ord("0")

    if(num <= 9):
        sumNum += num
    else:
        sumString += c

list(map(charToInt,string))

print(sumString+str(sumNum))