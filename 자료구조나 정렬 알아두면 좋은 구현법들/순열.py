def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    result = []

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            # result.append(chosen)
            # print(chosen)
            # print(''.join(map(str, chosen)))
            result.append(''.join(chosen))
            return

        # 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return result




ans = permutation('ABCD', 4)

print(ans)
# permutation([1, 2, 3, 4, 5], 3)

# def perm(data, depth, n, k):
#     if k == n:
#         pass
#     else:
#         for i in range(n):
#             for j in range(i+1, n):
#                 data[i], data[j] = data[j], data[i]
#                 perm(data,)


# def permutations(prefix,k):
#     if len(prefix) == r:
#         yield prefix
#     else:
#         for i in range(k,len(arr)):
#             arr[i], arr[k] = arr[k], arr[i]
#             for next in permutations(prefix + [arr[k]], k+1):
#                 yield next
#             arr[i], arr[k] = arr[k], arr[i]
#
# # 아래는 순열함수를 실행하기 위한 코드 예시 입니다.
# arr = [1,2,3,4,5]
# r = 3
# for perm in permutations([],0):
#     print(perm)