from collections import defaultdict

def perm():
    visited = [0] * (n+1)
    make_perm(visited, [])

def make_perm(visit, now_arr):
    if len(now_arr) == 3:
        tmp = sorted(now_arr)
        print(answer_list)
        if tmp not in answer_list:
            global answer
            answer += 1
            answer_list.append(tmp[:])
            return
        return
    for i in range(1, n+1):
        if not visit[i]:
            flag = True
            for j in range(len(now_arr)):
                if i in arr[now_arr[j]]:
                    flag = False
                    break
            if flag:
                visit[i] += 1
                now_arr.append(i)
                make_perm(visit, now_arr)
                now_arr.pop()
                visit[i] -= 1


n, m = map(int, input().split())
arr = defaultdict(list)
answer = 0
answer_list = []
for i in range(m):
    x, y = map(int, input().split())
    # arr.setdefault(x, [])
    arr[x].append(y)
    arr[y].append(x)
# print(arr)
perm()
# print(answer_list)
print(answer)

N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    unmixed = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        i, j = map(int, input().split())
        unmixed[i].append(j)
        unmixed[j].append(i)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in unmixed[i]:
                continue
            for k in range(j+1, N+1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                cnt += 1
    print(cnt)