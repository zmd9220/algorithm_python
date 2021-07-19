

def gen(num, value):
    check = [i for i in range(1, num+1)]
    da = []
    if value == 1:
        perm1(check, da)
    else:
        perm2(check, da)


def perm1(ch, data):
    global found, cnt, tmp2
    if found:
        return
    if len(data) == n:
        if cnt == arr[0]:
            found = True
            tmp2 = data.copy()
            # print(data, tmp2)
            return
        else:
            # print(data)
            cnt += 1
            return
    for i in range(n):
        if ch[i] != 0:
            tmp = ch[i]
            data.append(ch[i])
            ch[i] = 0
            perm1(ch, data)
            ch[i] = tmp
            data.pop()


def perm2(ch, data):
    global found, cnt, tmp2
    if found:
        return
    if len(data) == n:
        if data == arr:
            found = True
            tmp2 = cnt
            return
        else:
            # print(data)
            cnt += 1
            return
    for i in range(n):
        if ch[i] != 0:
            tmp = ch[i]
            data.append(ch[i])
            ch[i] = 0
            perm2(ch, data)
            ch[i] = tmp
            data.pop()


n = int(input())

arr = list(map(int, input().split()))
cnt = 1
found = False
if arr[0] == 1: # 뒤는 순열의 순서
    tmp3 = arr.pop(0)
    tmp2 = []
else: # 뒤는 순열
    tmp3 = arr.pop(0)
    tmp2 = 0
gen(n, tmp3)
if tmp3 == 1:
    for i in range(len(tmp2)):
        print(tmp2[i], end=" ")
else:
    print(tmp2)