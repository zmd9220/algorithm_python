
def is_babygin(data):
    is_run = 0
    for i in range(len(data)):
        # 트리플 여부
        if data[i] >= 3:
            return True
        # 런 여부
        if data[i] >= 1:
            is_run += 1
        else:
            is_run = 0
        if is_run >= 3:
            return True
    return False


for t in range(int(input())):
    arr = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    flag = False
    ans = 0
    for i in range(len(arr)):
        if i % 2:
            p2[arr[i]] += 1
            flag = is_babygin(p2)
            if flag:
                ans = 2
                break
        else:
            p1[arr[i]] += 1
            flag = is_babygin(p1)
            if flag:
                ans = 1
                break
    print('#{} {}'.format(t+1, ans))
