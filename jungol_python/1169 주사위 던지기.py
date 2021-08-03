def perm():
    arr = []
    visited = [0] * n
    if m == 1:
        make_perm(arr, visited)
    elif m == 2:
        make_perm2(arr, visited)
    else:
        make_perm3(arr, visited)


def make_perm(data, visit):
    if len(data) == n:
        print(' '.join(str(e) for e in data))
        return
    for i in range(1, 7):
        data.append(i)
        make_perm(data, visit)
        data.pop()


def make_perm2(data, visit):
    if len(data) == n:
        # print("change before: ", data)
        tmp = sorted(data)
        # print(tmp)
        if tmp not in ans:
            ans.append(tmp)
        return
    for i in range(1, 7):
        data.append(i)
        make_perm2(data, visit)
        data.pop()


def make_perm3(data, visit):
    if len(data) == n:
        print(' '.join(str(e) for e in data))
        return
    for i in range(1, 7):
        if i not in data:
            data.append(i)
            make_perm3(data, visit)
            data.pop()


n, m = map(int, input().split())
ans = []
perm()

if m == 2:
    # print(ans)
    for i in range(len(ans)):
        print(' '.join(str(e) for e in ans[i]))