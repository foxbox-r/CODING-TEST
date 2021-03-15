import sys
from collections import deque
input = sys.stdin.readline

# def showGraph(graph):
#     for i in range(1,len(graph)):
#         print(graph[i][1:])

N,M,K,X = map(int,input().split())

visit = [False]*(N+1)
graph = [([False] * (N+1)) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True

flag = False

def bfs():
    global flag

    q = deque([])
    q.append((0,X))

    while(q):
        curNode = q.popleft()
        curRow = graph[curNode[1]]
        if(curNode[0] == K):
            print(curNode[1])
            flag = True
            continue
        for i in range(1,len(curRow)):
            if curRow[i] and not visit[i]:
                q.append((curNode[0]+1,i))
                visit[i] = True

bfs()

if not flag:
    print(-1)
# 4 4 3 1
# 1 2
# 1 3
# 2 3
# 2 4