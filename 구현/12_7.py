import sys

input = sys.stdin.readline

string = input()

first,second = 0,0

for i in range(len(string)-1):
    if(i < (len(string)-1)/2):
        first += int(string[i])
    else:
        second += int(string[i])

print("LUCKY" if first == second else "READY")