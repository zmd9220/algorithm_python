import sys

n = int(sys.stdin.readline().rstrip())
st = list()
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        st.pop()
    else:
        st.append(a)

print(sum(st))