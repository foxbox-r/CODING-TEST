import sys
input = sys.stdin.readline

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def isSame(parent,a,b):
    if parent[a] == parent[b]:
        print("YES")
    else:
        print("NO")

n,m = map(int,input().split())

parent = []
for i in range(n+1):
    parent.append(i)

for _ in range(m):
    c,a,b = map(int,input().split())

    if c == 0:
        union_parent(parent,a,b)
    else:
        isSame(parent,a,b)
