# 시간이 좀 걸리지만 확실한 방법 - 모든 m*m 범위를 탐색해서 크기 비교
# 단 m*m을 할 때 x+m, y+m이 n보다 크게 되면 인덱스 에러가 나므로 주의(즉 m*m 계산을 하기엔 길이가 짧다는것)
for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if i + m <= n and j + m <= n:
                tmp = 0
                for k in range(i, i + m):
                    for l in range(j, j + m):
                        tmp += arr[k][l]
                if result < tmp:
                    result = tmp
    print(f'#{t+1} {result}')
