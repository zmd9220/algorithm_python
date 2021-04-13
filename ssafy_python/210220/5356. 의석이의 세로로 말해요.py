# 기본적으로 세로로 읽으므로 열 우선 탐색, 해당 열에 특정 행에 문자가 존재하는지 여부는 그 행의 길이로 판단하기(idx < len(행))
for t in range(int(input())):
    arr = [list(input()) for _ in range(5)]
    result = ''
    max_word = 0
    # 단순히 첫번째 행의 크기만큼 순회하는것도 방법이겠지만 만약 첫번째 행이 5문자의 단어, 그외에 행에서 5문자보다 큰 단어가 나온다면?
    # 그것을 고려하기 위해 해당 행들 중에서 최대 문자의 길이를 구해야함
    for i in range(len(arr)):
        if len(arr[i]) > max_word:
            max_word = len(arr[i])

    for i in range(max_word):
        for j in range(len(arr)):
            # 그 행의 전체 크기가 현재 확인하는 열 번호보다 커야만 찾기 가능
            if i < len(arr[j]):
                result += arr[j][i]

    print('#{} {}'.format(t+1, result))