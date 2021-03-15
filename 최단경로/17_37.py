import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 999999999
graph = [([inf]*(n+1)) for _ in range(n+1)]

def show(graph):
    for i in range(1,len(graph)):
        for j in range(1,n+1):
            if graph[i][j] != inf:
                print(graph[i][j],end=" ")
            else:
                print(0, end=" ")
        print("")

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for l in range(1,n+1):
            graph[j][l] = min(graph[j][l],graph[j][i]+graph[i][l])

show(graph)
