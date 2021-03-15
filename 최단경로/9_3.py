import sys
input = sys.stdin.readline

n,m,start = map(int,input().split())
inf = 9999999
graph = [[inf]*(n+1) for _ in range(n+1)]

def show(graph):
    for i in range(1,len(graph)):
        print(graph[i][1:])

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1,n+1):
    graph[i][i] = 0


for i in range(1,n+1):
    for j in range(1,n+1):
        for l in range(1,n+1):
            graph[j][l] = min(graph[j][l],graph[j][i]+graph[i][l])

first = -1
second = 0
for num in graph[start][1:]:
    if num != inf:
        first += 1
        second = max(second,num)

show(graph)
print(first,second)


