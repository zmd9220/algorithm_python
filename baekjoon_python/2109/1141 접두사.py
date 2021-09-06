
n = int(input())
arr = [input() for _ in range(n)]
sorted(arr)

sets = []
for i in range(len(arr)):
    tmp = [arr[i]]
    for j in range(i+1, len(arr)):
        flag = True
        for k in range(arr[j]):
            if arr[i][k] != arr[j][k]:
                flag = False
                break
        if flag:
            tmp.append(arr[j])
