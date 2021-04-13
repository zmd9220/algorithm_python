for t in range(int(input())):
    n, m = map(int, input().split())
    # cheese = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    # 각 피자별로 번호를 붙여줘야 관리하기 편할듯(enqueue, dequeue로 왔다갔다하니)
    for i in range(1, m+1):
        pizza[i-1] = [pizza[i-1], i]
    result = 0
    # 문제를 다시보니 화덕의 크기가 n 이었음 이걸 고려안함..
    oven = [pizza.pop(0) for _ in range(n)]
    while len(oven):
        # dequeue 해서 치즈 확인(반으로 녹음)
        now_pizza = oven.pop(0)
        cheese = now_pizza[0] // 2
        # 치즈가 1 이상(치즈가 남음) 다시 넣기(반으로 쪼갠 값으로)
        if cheese:
            now_pizza[0] = cheese
            oven.append(now_pizza)
        # 조금 시간잡아먹지만 확실하게(매번 피자번호 갱신, 마지막에 나올 피자번호가 최종결과값)
        else:
            # print(now_pizza, pizza)
            result = now_pizza[1]
            # 동시에 아직 구워야할 피자가 남았으면 오븐에 넣기
            if len(pizza):
                oven.append(pizza.pop(0))

    print('#{} {}'.format(t+1, result))