T = int(input())

for t in range(T):
    n = int(input())
    a = int(input())
    arr = [0] * 10 # 0 ~ 9 를 카운팅 하는 배열
    # 고전적 방법(c, 자바에서 썼던)
    while a > 0:
        # 10의 나머지를 통해 카드 갯수를 하나씩 카운팅
        arr[a % 10] += 1
        a //= 10
    max_card = 9 # 가장 많은 카드 - 디폴트 가장 큰 카드인 9번
    max_num = arr[9] # 카드 장 수 - 디폴트 가장 큰 카드의 갯수인 9번의 갯수
    # 맨 뒤 부터 탐색해야 같은 카드 장수일때 가장 큰 수가 출력됨
    # len(arr)-2는 9번 카드는 이미 적었기 때문에 비교할 필요가 없음
    for i in range(len(arr)-2, -1, -1):
        # 가장 많은 카드를 찾는 과정
        if arr[i] > max_num:
            max_num = arr[i]
            max_card = i

    print(f'#{t+1} {max_card} {max_num}')
    # 스트링으로 받아서 슬라이싱이나 인덱스접근으로도 입력을 받을 수 있음
    # a = input()
    # arr = [0] * 10
    # for char in a:
    #     arr[int(char)] += 1



