import sys

class Stack:
    def __init__(self):
        self.dt = [0 for i in range(10001)]
        self.index = 0
        self.size = 0

    def isSize(self):
        print(self.size)

    def empty(self):
        if self.size == 0:
            print(1)
        else:
            print(0)

    def push(self, x):
        self.dt[self.index] = x
        self.index += 1
        self.size += 1

    def pop(self):
        if self.size == 0:
            print(-1)
        else:
            data = self.dt[self.index-1]
            self.dt[self.index-1] = 0
            self.index -= 1
            self.size -= 1
            print(data)

    def top(self):
        if self.size == 0:
            print(-1)
        else:
            data = self.dt[self.index-1]
            print(data)


n = int(sys.stdin.readline().rstrip())
st = Stack()
for i in range(n):
    line = list(sys.stdin.readline().rstrip().split())
    if line[0] == 'push':
        st.push(int(line[1]))
    elif line[0] == 'top':
        st.top()
    elif line[0] == 'pop':
        st.pop()
    elif line[0] == 'empty':
        st.empty()
    else:
        st.isSize()
