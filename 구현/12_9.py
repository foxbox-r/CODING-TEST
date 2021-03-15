string = "aabbaccc"
# "aabbccc","xababcdcdababcdcd"

def split(data):
    string = data[0]
    n = data[1]
    arr = []
    for i in range(len(string)//n):
        index = i * n
        arr.append(string[index:index+n])
    if len(string)%n != 0:
        arr.append(string[-(len(string)%n):len(string)])
    data[0] = arr

def comp(arr):

    if(len(arr) == 1):
        return arr[0]

    string = ""
    prev = arr[0]
    cur = ""
    count = 1
    for i in range(1,len(arr)):
        cur = arr[i]
        if prev == cur:
            count += 1
        else:
            if count == 1:
                string += prev
            else:
                string += str(count) + prev
            count = 1
            prev = cur
    if count == 1:
        string += cur
    else:
        string += str(count) + cur

    return string

def press(_str,n):
    string = _str[0:len(_str)]

    data = [string,n]
    split(data)
    return comp(data[0])

def stringToLength(str):
    return len(str)


arr = []
for i in range(1,len(string)+1):
    arr.append(press(string,i))

lenArr = list(map(stringToLength,arr))
lenArr.sort()

print(lenArr[0])