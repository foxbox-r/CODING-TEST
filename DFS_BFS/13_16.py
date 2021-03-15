from copy import deepcopy
import sys
input = sys.stdin.readline

Row,Col = map(int,input().split())

graph = []

arr_find_2 = []

x_d = [0,0,-1,1]
y_d = [-1,1,0,0]

def showGarph(graph):
    for i in range(len(graph)):
        print(graph[i])

def dfs(position,graph):
    for i in range(4):
        n_y = position[0] + y_d[i]
        n_x = position[1] + x_d[i]
        if n_y != -1 and n_x != -1 and n_y != Row and n_x != Col and graph[n_y][n_x] == 0:
            graph[n_y][n_x] = 2
            dfs((n_y,n_x),graph)

def find_2():
    for i in range(Row*Col):
        row = i // Col
        col = i % Col
        if graph[row][col] == 2:
            arr_find_2.append((row,col))

def getMaxNumber(graph):

    for position in arr_find_2:
        dfs(position,graph)
    # showGarph(graph)
    count = 0

    for i in range(Row * Col):
        row = i // Col
        col = i % Col
        if graph[row][col] == 0:
            count += 1
    return count

for _ in range(Row):
    arr = list(map(int,input().split()))
    graph.append((arr))

find_2()

result = 0

for i_1 in range(Row*Col):
    row_1 = i_1 // Col
    col_1 = i_1 % Col
    if graph[row_1][col_1] != 0:
        continue
    for i_2 in range(Row*Col):
        row_2 = i_2 // Col
        col_2 = i_2 % Col
        if graph[row_2][col_2] != 0:
            continue
        for i_3 in range(Row*Col):
            row_3 = i_3 // Col
            col_3 = i_3 % Col
            if graph[row_3][col_3] != 0:
                continue
            copy_graph = deepcopy(graph)
            index_arr = [[row_1,col_1],[row_2,col_2],[row_3,col_3]]

            for position in index_arr:
                copy_graph[position[0]][position[1]] = 1

            result = max(result,getMaxNumber(copy_graph))

print(result)
