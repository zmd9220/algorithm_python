T = int(input())
for t in range(T):
    n = int(input())
    nums = [0] * 10  # 0~9까지 숫자 집어넣기
    cnt = 1
    while True:
        tmp = n * cnt
        while tmp > 0:
            # 자리수 별로 나눠서 해당 숫자가 배열의 0~9번 숫자 중에 한번도 안들어온 숫자라면 최초로 추가
            # 더 추가해도 이 문제에서는 상관이 없지만 안해도 됨
            if nums[tmp % 10] == 0:
                nums[tmp % 10] += 1
            tmp //= 10
        # 모든 배열에 1이 들어갔을 때 - 모든 숫자 확인
        if not 0 in nums:
            break
        cnt += 1
    print(f'#{t+1} {cnt*n}')
