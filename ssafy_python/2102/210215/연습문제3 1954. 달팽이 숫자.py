arr = [[0]*5 for i in range(5)]

# cnt = 1
# for i in range(5):
#     for j in range(5):
#         arr[i][j] = cnt
#         cnt += 1

# row_start, col_start = 0, 0
# row_end, col_end = len(arr)-1, len(arr)-1
# row_now, col_now = 0, 0
# cnt = 1
# while True:
#     if row_now < row_end:
#         arr[col_now][row_now] = cnt
#         row_now += 1
#         if row_now == row_end:
#             row_start += 1
#     elif col_now < col_end:
#         arr[col_now][row_now] = cnt
#         col_now += 1
#         if col_now == col_end:
#             col_start += 1
#     elif row_now > row_start:
#         arr[col_now][row_now] = cnt
#         row_now -= 1
#         if row_now == row_start:
#             row_start += 1
#     elif col_now > col_start:
#         arr[col_now][row_now] = cnt
#         col_now -= 1
#         if col_now == col_start:
#             col_start += 1
#
#     cnt += 1





print(arr)