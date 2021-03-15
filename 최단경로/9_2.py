import sys
input = sys.stdin.readline

n,m = map(int,input().split())

inf = 9999999
graph = [([inf]*(n+1)) for _ in range(n+1)]

for _ in range(m):
    a,b= map(int,input().split())
    graph[a][b] = graph[b][a] = 1

x,k = map(int,input().split())

for i in range(1,n+1):
    graph[i][i] = 0

def show(graph):
    for i in range(1,len(graph)):
        print(graph[i][1:])

for i in range(1,n+1):
    for j in range(1,n+1):
        for l in range(1,n+1):
            graph[j][l] = min(graph[j][l],graph[j][i]+graph[i][l])

show(graph)

result = graph[1][k] + graph[k][x]

print(result if result < inf else -1)

#  3
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

#  -1
# 4 2
# 1 3
# 2 4
# 3 4