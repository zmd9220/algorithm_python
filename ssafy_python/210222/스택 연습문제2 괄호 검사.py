
string = input()
st = []
for i in range(len(string)):
    if string[i] == '(':
        st.append(string[i])
    else:
        if len(st) == 0:
            print('"(" 괄호 부족')
            break
        else:
            st.pop()
if len(st):
    print('"(" 괄호가 남음')
else:
    print('정상적인 괄호')