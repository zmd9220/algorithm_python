# 0F97A3
# 01D06079861D79F99F

# 16진수 테이블 만들거나, 일일히 변환하거나
hex_table = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',
}

hex_arr = input()
str_arr = ''
for i in range(len(hex_arr)):
    str_arr += hex_table[hex_arr[i]]
print(str_arr)

for i in range(0, len(str_arr), 7):
    ans = 0
    tmp_arr = str_arr[i:i+7]
    # print(tmp_arr)
    for j in range(len(tmp_arr)-1, -1, -1):
        ans += int(tmp_arr[len(tmp_arr)-j-1]) * (2 ** j)
    print(ans)