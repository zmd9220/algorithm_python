# visited 리스트로 방문여부 체크 or 스택으로 dfs 정점 관리 하되 한번 방문하면 해당 위치를 1로 변경 둘 중에 하나 사용
def dfs(data, first):
    # 방향
    delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    stack = [[first[0], first[1]]]
    # 각 방향별로 더하고 그지점이 0인 경우 스택 추가 1이면 패스 3이면 1리턴
    while len(stack):
        now_idx = stack.pop()
        for d in delta:
            x, y = now_idx[0]+d[0], now_idx[1]+d[1]
            if data[x][y] == 0:
                stack.append([x, y])
                # 0을 사용했으니 좌표값을 1로 변경해주면 다시 사용안함
                data[x][y] = 1
            elif data[x][y] == 3:
                return 1
    return 0

for t in range(int(input())):
    start = ()
    n = int(input())
    # 5*5 미로라면 7*7로 만들되 상하좌우 끝에 모두 1로 만들기 - 나중에 조건넣기 편해짐
    arr = [[1] * (n+2)]
    for i in range(n):
        case = input()
        # 양쪽 끝에 1로 벽을 새로 세워둠 나중에 관리가 편해짐
        tmp = [1]
        # 값을 스트링으로 받아 정수형으로 나눠서 2차원 배열로 만들기 - 이때 스타트 지점도 같이구함
        for j in range(len(case)):
            # 스타트지점
            if int(case[j]) == 2:
                # n+2*n+2배열로 만들었으므로 index 시작지점 변경에 주의
                start = (i+1, j+1)
                tmp.append(int(case[j]))
            else:
                tmp.append(int(case[j]))
        tmp.append(1)
        arr.append(tmp)
    arr.append([1] * (n+2))
    print('#{} {}'.format(t+1, dfs(arr, start)))
    # print(start)
    # print(arr[start[0]][start[1]])