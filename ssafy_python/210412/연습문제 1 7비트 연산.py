# 0000000111 1000000110 0000011110 0110000110 0001111001 1110011111 1001100111
# 0000000111100000011000000111100110000110000111100111100111111001100111
arr = input()


for i in range(0, len(arr), 7):
    ans = 0
    tmp_arr = arr[i:i+7]
    for j in range(len(tmp_arr)-1, -1, -1):
        ans += int(tmp_arr[len(tmp_arr)-j-1]) * (2 ** j)
    print(ans)