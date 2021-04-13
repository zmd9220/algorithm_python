from itertools import permutations


def permutation(num):
    data = [ns for ns in range(num)]
    result = [data[:]]
    tmp = [0] * len(data)
    idx = 0
    while idx < len(data):
        if tmp[idx] < idx:
            if idx % 2 == 0:
                data[0], data[idx] = data[idx], data[0]
            else:
                data[tmp[idx]], data[idx] = data[idx], data[tmp[idx]]
            result.append(data[:])
            tmp[idx] += 1
            idx = 0
        else:
            tmp[idx] = 0
            idx += 1
    return result


for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_value = 99999999
    # per_arr = permutation(n)
    # print(per_arr)
    # for per_list in per_arr:
    #     per_sum = 0
    #     for i in range(n):
    #         per_sum += arr[i][per_list[i]]
    #         if per_sum > min_value:
    #             break
    #     if per_sum < min_value:
    #         min_value = per_sum

    for per_list in permutations(range(n)):
        per_sum = 0
        for i in range(n):
            per_sum += arr[i][per_list[i]]
            if per_sum > min_value:
                break
        if per_sum < min_value:
            min_value = per_sum

    print('#{} {}'.format(t+1, min_value))

