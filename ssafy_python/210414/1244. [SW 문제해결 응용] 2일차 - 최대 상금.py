import sys

sys.stdin = open("input.txt", "r")

for t in range(int(input())):
    # n, m = map(int, input().split())
    n, m = input().split()
    arr = list(map(int, n))
    m = int(m)
    # print(arr)
    search_idx = 0
    # max_val_count = arr.count(max(arr))
    while m:
        # print(search_idx)
        # flag = 현재 인덱스에 존재하는 값이 위치해야할 곳에 정확히 있을 때 변경은 일어나지 않으므로 m을 빼지 않도록 체크
        flag = False
        max_idx = search_idx

        # 아직 search_idx가 배열 끝까지 도착하지 않았을 때 (정렬이 완료되지 않았을 때)
        if search_idx < len(arr):
            for j in range(search_idx+1, len(arr)):
                if arr[max_idx] <= arr[j]:
                    # if arr[search_idx]
                    max_idx = j
                    flag = True
                # elif
            max_idx_count = arr.count(arr[max_idx])
            change_length = 0
            if max_idx_count > 1:
                for i in range(search_idx, len(arr)):
                    if arr[search_idx] >= arr[i]:
                        change_length += 1
                    else:
                        break
                change_length = min(change_length, max_idx_count, m)
                for i in range(change_length-1, -1 , -1):
                    if arr[search_idx] == arr[max_idx-i]:
                        search_idx += i
                        break
                    arr[search_idx], arr[max_idx-i] = arr[max_idx-i], arr[search_idx]
                    search_idx += 1
                m -= change_length
                continue


        # 정렬 완료인 상태에서 m이 남았으면 m이 남은게 짝수냐 홀수냐에 따라 갈림
        else:
            # 짝수면 동일 위치를 짝수번 바꾸면 그대로 위치이므로 이제 변동 필요 X
            if m % 2 == 0:
                break
            else:
                # 홀수면 최선은 같은 자리의 카운트가 2개이상 있을 경우 둘이 바꾸면 그대로의 값이 됨
                # 즉 이제 더 돌 필요가 없다는 말 -> m = 0
                for i in range(len(arr)):
                    if arr.count(arr[i]) >= 2:
                        m = 0
                        break
                # 그 다음은 1의 자리와 10의 자리를 바꾸는게 최선
                search_idx -= 1
                max_idx = search_idx - 1
                flag = True
        if flag:
            # print(search_idx, max_idx)
            arr[search_idx], arr[max_idx] = arr[max_idx], arr[search_idx]
            m -= 1
        search_idx += 1
        # print(arr)
    print('#{} {}'.format(t+1, ''.join(map(str, arr))))

    # print(arr)

    # while n:
    #     arr.append(n % 10)
    #     n //= 10
    # print(arr)
    # for i in range(m):
    #     max_idx = i
    #     for j in range(1, len(arr)):
            # if int(n[max_idx]) < int(n[j]):
            #     max_idx = j


