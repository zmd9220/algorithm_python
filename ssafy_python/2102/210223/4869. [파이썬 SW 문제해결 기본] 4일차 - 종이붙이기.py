# 점화식 f(n) = f(n-1) + 2(f(n-2))
# 왜냐면 항상 마지막에 붙여지는 경우는
# 10짜리 한개 세로로 붙이는 경우, 10짜리를 가로로 2개로 나열해서 붙이는 경우, 20*20짜리를 마지막에 붙이는 경우
# 그러면 n기준의 경우의 수는 n-1의 가짓수 + n-2의 가짓수2개이다.
# 더불어 메모이제이션으로 미리 계산해도 가능한 문제
def dp(num):
    arr = [1, 1]
    if num > 1:
        for i in range(2, num+1):
            arr.append(arr[i-1] + 2*(arr[i-2]))
    return arr


arr = dp(30)
for t in range(int(input())):
    n = int(input())
    print('#{} {}'.format(t+1, arr[n//10]))