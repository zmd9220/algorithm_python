class Stack:
    tp = -1
    arr = []

    def push(self, num):
        self.arr.append(num)
        self.tp += 1

    def pop(self):
        self.tp -= 1
        return self.arr.pop()

    def top(self):
        return self.arr[self.tp]


st = Stack()
st.push(1)
st.push(2)
st.push(5)
print(st.top())
for _ in range(3):
    print(st.pop())
