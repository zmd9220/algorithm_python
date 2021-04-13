# 일반 이진트리를 구현하는 법
# 1. 자식을 관리하는 배열 따로 만들기
# 2. n*2, n*2+1를 이용한 1차원 배열쓰기
# 3. 자식에 아예 부모 인덱스를 넣기
def postorder(tr, n):
    # 해당 값이 수 인 경우 바로 리턴, 연산자 일 경우 순회해서 값 알아내기
    if tr[n].isdigit():
        return int(tr[n])
    # 연산자 일 경우 자식은 무조건 있음 - 없으면 식이 성립하지 않음 left, right if문 안써도 되긴한데 혹시모르니
    else:
        if child[n][0] != 0:
            left = postorder(tr, child[n][0])
        if child[n][1] != 0:
            right = postorder(tr, child[n][1])
        if tr[n] == '+':
            return left + right
        elif tr[n] == '-':
            return left - right
        elif tr[n] == '*':
            return left * right
        else:
            return left // right


for t in range(1, 11):
    n = int(input())
    tree = [''] * (n+1)
    child = [[0] * 2 for _ in range(n+1)]
    for i in range(n):
        test = list(input().split())
        idx = int(test[0])
        tree[idx] = test[1]
        for j in range(2, len(test)):
            if child[idx][0] == 0:
                child[idx][0] = int(test[j])
            else:
                child[idx][1] = int(test[j])
    ans = postorder(tree, 1)
    print(f'#{t} {ans}')

# for t in range(1, 11):
#     n = int(input())
#     tree = [''] * (n * 2 + 2)
#     for i in range(n):
#         test = list(input().split())
#         tree[int(test[0])] = test[1]
#         # left = tree[int(test[0]) * 2]
#         # right = tree[int(test[0]) * 2 + 1]
#         for j in range(2, len(test)):
#             # 좌, 우 자식 채워 넣기
#             if tree[(int(test[0]) * 2)] != '':
#                 tree[(int(test[0]) * 2) + 1] = test[j]
#             else:
#                 tree[(int(test[0]) * 2)] = test[j]
#             # if int(test[0]) == 56:
#             #     print('value:', tree[(int(test[0]) * 2) + 1], 'tt',(int(test[0]) * 2) + 1)
#             #     print(tree[(int(test[0]) * 2)], (int(test[0]) * 2))
#     ans = postorder(tree, 1)
#     print(f'#{t} {ans}')


# T = 10
# for t in range(1,T+1):
#     N = int(input())
#     arr = [0] + [list(input().split()) for _ in range(N)]
#     node = [0] * (N+1)
#     for i in range(N,0,-1):
#         # 사칙연산이면 뒤에 자식노드 존재 -> 계산
#         if arr[i][1] in '+-*/':
#             A, B = int(arr[i][2]), int(arr[i][3])
#             if arr[i][1] == '+':
#                 node[i] = node[A] + node[B]
#             elif arr[i][1] == '-':
#                 node[i] = node[A] - node[B]
#             elif arr[i][1] == '*':
#                 node[i] = node[A] * node[B]
#             else:
#                 node[i] = node[A] / node[B]
#         # 숫자면 node에 그대로 추가
#         else:
#             node[i] = int(arr[i][1])
#     ans = int(node[1])
#     print(f'#{t} {ans}')