# 숫자를 받아 문자에 해당할 경우 변환 만약 음수라면 * -1 해주면됨

ls = [23, 65, 66, 67, 70, 94, 96, 97, 101]
st = ''
for i in range(len(ls)):
    if ord('A') <= ls[i] <= ord('Z') or ord('a') <= ls[i] <= ord('z'):
        st += chr(ls[i])
print(st)
