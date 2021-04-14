# 이중리스트로 풀기?
for t in range(int(input())):
    # 전체 이중리스트
    arr = []
    n = int(input())
    print('#{}'.format(t+1))
    for i in range(n):
        # 각 행마다 리스트로 정리
        ls = []
        for j in range(i+1):
            # 양 끝은 1
            if j == i or j == 0:
                ls.append(1)
            # 끝이 아닐경우 내 기준 위의 왼쪽과 오른쪽 j-1, j
            else:
                ls.append(arr[i-1][j-1] + arr[i-1][j])
        # 각각 처리가 끝날때마다 완성된 행을 이중리스트에 넣기
        print(' '.join(map(str, ls)))
        arr.append(ls)
