
arr = []
st = '2+3*4/5'
for i in range(len(st)):
    if ord('0') <= ord(st[i]) <= ord('9'):
        print(st[i], end='')
    else:
        arr.append(st[i])
for i in range(len(arr)):
    print(arr.pop(), end='')
