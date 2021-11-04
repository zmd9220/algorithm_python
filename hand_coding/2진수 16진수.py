
word = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def make_nums(num):
    two_num = num
    two_ans = ''
    while two_num:
        # if two_num == 1:
        #     two_ans += str(two_num)
        two_ans += str(two_num % 2)
        two_num //= 2
    print(two_ans[::-1])

    six_num = num
    six_ans = ''
    while six_num:
        if six_num % 16 >= 10:
            six_ans += word[six_num % 16]
        else:
            six_ans += str(six_num % 16)
        six_num //= 16
    print(six_ans[::-1])

make_nums(2)
make_nums(16)
make_nums(15)