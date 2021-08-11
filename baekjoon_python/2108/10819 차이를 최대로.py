
def perm():
    data = []
    visited = [0] * n
    make_perm(data, visited)


def make_perm(data, visited):
    if len(data) == n:
        tmp_value = 0
        for i in range(1, n):
            tmp_value += abs(data[i-1] - data[i])
        global ans
        if ans < tmp_value:
            ans = tmp_value
        return
    for i in range(n):
        if not visited[i]:
            data.append(arr[i])
            visited[i] = 1
            make_perm(data, visited)
            data.pop()
            visited[i] = 0


n = int(input())
arr = list(map(int, input().split()))
ans = 0
perm()
print(ans)