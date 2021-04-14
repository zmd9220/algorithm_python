# 함수로 푸는법
def palindrome(arr):
    for pal in range(100, 0, -1):
        # 현 문제에서 최대 회문은 100단어 큰 수 부터 줄여나가는 식으로 해서 가장 먼저 만나는 큰 수 회문이 가장 큰 회문
        # 그 이후의 회문은 다 작으므로 구할 필요가 없어짐
        for i in range(100):
            for j in range(100 - pal + 1):
                # 회문 판독 for문으로 하는 방법도 있고
                # 슬라이싱으로 비교하는 법도 있지만 여기서는 슬라이싱으로 진행
                # 0~pal 까지의 문자열이 그것의 역과 같다면 == 회문을 찾음
                if arr[i][j:j + pal] == arr[i][j:j + pal][::-1]:
                    return pal

for t in range(10):
    n = int(input())
    arr = [input() for _ in range(100)]
    # 전체 회문은 m 크기여야 하므로 n-m 인덱스 이상의 인덱스들의 문자열은 m보다 작은 문자열이 됨
    # 단 현재 range의 경우 해당 숫자 전까지 이므로 +1 해주기
    # 또 가로 비교 세로 비교 두가지 경우로 나눠서 진행
    # 가로
    result = palindrome(arr)
    # 세로를 슬라이싱 하기 위한 배열 생성
    col_arr = []
    for i in range(100):
        tmp_col = ''
        for j in range(100):
            tmp_col += arr[j][i]
        col_arr.append(tmp_col)
    # 세로
    result2 = palindrome(col_arr)
    if result < result2:
        result = result2
    print('#{} {}'.format(t + 1, result))

# # 전체 비교 다쓰는 법
# for t in range(10):
#     n = int(input())
#     arr = [input() for _ in range(100)]
#     # 전체 회문은 m 크기여야 하므로 n-m 인덱스 이상의 인덱스들의 문자열은 m보다 작은 문자열이 됨
#     # 단 현재 range의 경우 해당 숫자 전까지 이므로 +1 해주기
#     # 또 가로 비교 세로 비교 두가지 경우로 나눠서 진행
#     result = 0
#     # 1. 가로 비교는 슬라이싱 덕에 쉬운편
#     for pal in range(100, 0, -1):
#         # 현 문제에서 최대 회문은 100단어 큰 수 부터 줄여나가는 식으로 해서 가장 먼저 만나는 큰 수 회문이 가장 큰 회문
#         # 그 이후의 회문은 다 작으므로 구할 필요가 없어짐
#         # found가 모든 for문 탈출 조건
#         found = False
#         for i in range(100):
#             for j in range(100-pal + 1):
#                 # 회문 판독 for문도 있고 그냥 슬라이싱 비교 0~pal 까지의 문자열이 그것의 역과 같다면 == 회문을 찾음
#                 if arr[i][j:j+pal] == arr[i][j:j+pal][::-1]:
#                     found = True
#                     # result = len(arr[i][j:j+pal])
#                     result = pal
#                     break
#             # 회문을 찾아낸 다음 처리
#             if found:
#                 break
#         # result 값이 0이 아니다 = 회문을 찾아서 값이 변경됐다 = 더 돌 필요가 없다
#         # 생각해보니 found도 어차피 true 한번만 되면 모두 종료하므로 변경
#         if found:
#             break
#
#     # 2. 세로 비교는 슬라이싱이 안돼서 조금 더 복잡.. 혹은 세로를 위한 리스트(세로를 가로로 만든 리스트라고 생각하면됨 - 왼쪽으로 90도 꺾은 모습?)를 만들어서 가로와 같이 슬라이싱해서 풀기
#     col_arr = []
#     for i in range(100):
#         tmp_col = ""
#         for j in range(100):
#             tmp_col += arr[j][i]
#         col_arr.append(tmp_col)
#
#     for pal in range(100, 0, -1):
#         # 현 문제에서 최대 회문은 100단어 큰 수 부터 줄여나가는 식으로 해서 가장 먼저 만나는 큰 수 회문이 가장 큰 회문
#         # 그 이후의 회문은 다 작으므로 구할 필요가 없어짐
#         # 세로의 경우 이미 result에 값이 있는 상태로 시작하기 때문에 i for문을 탈출하기 위한 조건을 따로 지정
#         # 다시보니 found를 i의 변수로 두면 됨
#         found = False
#         for i in range(100):
#             for j in range(100 - pal + 1):
#                 # 회문 판독 for문도 있고 그냥 슬라이싱 비교 0~pal 까지의 문자열이 그것의 역과 같다면 == 회문을 찾음
#                 if col_arr[i][j:j + pal] == col_arr[i][j:j + pal][::-1]:
#                     found = True
#                     # 세로의 경우 작은지 큰지 비교
#                     # if result < len(col_arr[i][j:j + pal]):
#                     #     result = len(col_arr[i][j:j + pal])
#                     if result < pal:
#                         result = pal
#                     break
#             # 회문을 찾아낸 다음 처리
#             if found:
#                 break
#         if found:
#             break
#
#     print('#{} {}'.format(t + 1, result))

# for _ in range(10) :
#     T = int(input())
#     board = []
#     for _ in range(100) :
#         board.append(input())
#
#     def check(string, length) :
#         max = length
#         while(length <= 100) :
#             answer = 0
#             for i in range(100) :
#                 for j in range(101-length) :
#                     word = string[i][j:j+length]
#                     if word == word[::-1] :
#                         max = length
#                         answer = 1
#                         break
#                 if answer == 1 :
#                     break
#             length += 1
#         return max
#
#     # 가로줄
#     row = check(board, 1)
#
#     # 세로줄
#     transposed_board = []
#     for i in range(100) :
#         list = ""
#         for j in range(100) :
#             list += board[j][i]
#         transposed_board.append(list)
#
#     col = check(transposed_board, 1)
#
#     print("#{} {}".format(T, max(row, col)))


# # 단어 리스트 안에서 len_word 만큼의 단어가 회문인지 판단
# # 회문일 경우 단어 길이를 리턴하는 함수
# def len_palindrome(word_list, len_word):
#     # 100 줄 문장을 순회하는 for loop
#     for i in range(len(word_list)):
#         # 단어의 길이만큼 인덱싱을 조절하는 for loop
#         for j in range(100 - len_word + 1):
#
#             # 회문 판단을 위해 단어 길이를 2로 나눠 인덱스로 접근
#             # j+k, j+len_word-1-k는 k가 커질수록 양 끝에서 중앙으로 접근하며 비교
#             for k in range(len_word // 2):
#                 if word_list[i][j + k] != word_list[i][j + len_word - 1 - k]:
#                     break
#             else:
#                 return len_word
#     # 회문을 찾지 못했다면 0을 출력
#     return 0
#
#
# # 리스트 속에서 가장 긴 회문의 길이를 찾는 함수
# # 초기 회문의 길이는 1로 설정
# def find_max_len(word_list, len_pal=1):
#     # 길이 2부터, 100까지의 for loop 순회
#     for i in range(len_pal + 1, 101):
#         # 2) 만일 현재 할당된 회문 길이인 len_pal보다 i가 2이상 커진다면 중단
#
#         # 회문은 무조건 2씩 늘어나기 때문에 다음과 같이 지정
#         if i > len_pal + 2:
#             break
#         # 3글자의 회문이라면 5글자가 회문인지 판단, 아니면 더이상 회문 없음
#         # 4글자의 회문이라면 6글자가 회문인지 판단, 아니면 더이상 회문 없음
#
#         # 1) 만일 현재 회문의 길이 값보다 i 길이 단어가 회문이면서 크다면, i를 새로 할당
#         if len_pal < len_palindrome(word_list, i):
#             len_pal = i
#     return len_pal
#
#
# x = 0
# while x < 10:
#     tc = int(input())
#     _list = [input() for _ in range(100)]
#     vertical_list = [''.join(_) for _ in zip(*_list)]
#
#     row_max_len = find_max_len(_list)
#     result = find_max_len(vertical_list, row_max_len)
#
#     print('#{} {}'.format(x + 1, result))
#     x += 1