import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    d = list(sys.stdin.readline().rstrip())
    flag = 0
    st = list()
    for j in range(len(d)):
        ch = d.pop()
        if ch == '(':
            if len(st) == 0:
                print('NO')
                flag = 1
                break
            else:
                st.pop()
        else:
            st.append(ch)
    if flag == 1:
        continue
    if len(st) == 0:
        print('YES')
    else:
        print('NO')