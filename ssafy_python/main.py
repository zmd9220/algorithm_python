for i in range(3):
    print(i)

data=[7, 4, 2, 0, 0, 6, 0, 7, 0]
MAX=0
for i in range(9):
    cnt = 0
    for j in range(i+1, 9):
        if data[i]>data[j]:
            cnt+=1
    if MAX<cnt:
        MAX=cnt
print(MAX)

from random import*
def build_data():
    for i in range(0, 100):
        data[i]=randint(0, 100)
data=[0]*100
MAX=-99999999
build_data()
for i in range(100):
    cnt = 0
    for j in range(i+1, 100):
        if data[i]>data[j]:
            cnt+=1
    if MAX<cnt:
        MAX=cnt
print(MAX)