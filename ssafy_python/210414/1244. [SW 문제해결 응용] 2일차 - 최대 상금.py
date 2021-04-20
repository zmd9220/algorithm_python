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


# # D3 1244 최대상금
#
# # 경우의 수 찾기, 매개변수로 몇번 바꿧는지 적는다.
# def dfs(count):
#     global answer
#     # 횟수를 다 사용했다면
#     if not count:
#         # 숫자로 바꿔보고
#         temp = int(''.join(values))
#         # 가지고 있는 최대수보다 크다면 갱신
#         if answer < temp:
#             answer = temp
#         return
#     # 바꿔야 하니까 이중 포문
#     for i in range(length):
#         # 경우의 수를 찾는거니까 i보다 큰위치부터
#         for j in range(i + 1, length):
#             # 두개의 위치를 바꾸고 나서
#             values[i], values[j] = values[j], values[i]
#             # 가지치기 해야하니까 일단 합쳐보고
#             temp_key = ''.join(values)
#             # 어떤수가 몇회차에 나왔는지 체크 1이면 안나온거니까 경우의수에 넣어주기
#             if visited.get((temp_key, count - 1), 1):
#                 # 이숫자는 몇회차에 사용했으니까 체크해주고
#                 visited[(temp_key, count - 1)] = 0
#                 # dfs도 돌려주고
#                 dfs(count - 1)
#             # 다 썻으면 원상복귀
#             values[i], values[j] = values[j], values[i]
#
#
# for t in range(int(input())):
#     answer = -1
#     value, change = input().split()
#     # 바꾸기 편하려고 리스트화시킴
#     values = list(value)
#     change = int(change)
#     # 계속 쓸꺼니까 캐스팅
#     length = len(values)
#     # 가지치기용 딕셔너리
#     visited = {}
#     dfs(change)
#     print('#{} {}'.format(t + 1, answer))


# def dfs(d, cnt):
#     global ret
#     if cnt == n:
#         ret = max(int("".join(nums)), ret)
#         return
#     for i in range(d, l):
#         for j in range(i + 1 , l):
#             if nums[i] <= nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 dfs(i, cnt + 1)
#                 nums[i], nums[j] = nums[j], nums[i]
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     nums, n = input().split()
#     nums = list(nums)
#     numbers = nums[:]
#     n = int(n)
#     l = len(nums)
#     ret = 0
#     flag = 0
#     if len(nums) == 2 or nums == sorted(nums, reverse=True):
#         cnt = 0
#         while cnt != n:
#             numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
#             cnt += 1
#         flag = int("".join(numbers))
#     cnt = 0
#     dfs(0, cnt)
#     if ret == 0:
#         ret = flag
#     print("#" + str(test_case) + " " + str(ret))