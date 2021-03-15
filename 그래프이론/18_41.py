import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())

parent = [0]

for i in range(1,n+1):
    parent.append(i)

for i in range(1,n+1):
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            if find_parent(parent,i) != find_parent(parent,j+1):
                union_parent(parent,i,j+1)

for i in range(n+1):
    find_parent(parent,i)

plan = list(map(int,input().split()))
print("YES")
firstPlan = parent[plan[0]]
for v in plan[1:m]:
    if firstPlan != parent[v]:
        print("NO")
        break
    else:
        print("YES")

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3