
for t in range(int(input())):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    # print(trucks, containers)
    # 그리디 해당 케이스에 있어서의 최선 값을 가져가서 푸는 문제 - 단 이것이 모든 케이스의 정답이 될 순 없다.
    # 여기서 트럭은 컨테이너 '1개'만 가져갈 수 있고 편도이므로 1번만 가져갈 수 있으므로 자신이 가져갈 수 있는 최대 값을 가져가는 것이 가장 좋음
    # 만약 2개 이상이라면 그리디 알고리즘으로 풀 수 없다.
    # 해당 트럭에 맞춰서 가장 최대값이 되는 크기를 구하고, 그것을 dp에 저장하든지, 값을 넣는 식으로 구현해야함
    ans = 0
    # count = 0
    for i in range(m):
        for j in range(len(containers)):
            if trucks[i] >= containers[j]:
                ans += containers[j]
                containers.pop(j)
                # count += 1
                break
        # if count == m:
        #     break
    print('#{} {}'.format(t+1, ans))

