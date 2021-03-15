
def solution(array, commands):
    result = []

    narr = []
    for arr in commands:
        start,end,nth = arr
        narr = array[start-1:end-1]
        narr.sort()
        print(narr)
        result.append(narr[nth-1])
    return result

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))