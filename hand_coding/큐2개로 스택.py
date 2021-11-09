from queue import Queue
from collections import deque
class stack:
    q1 = Queue()
    q2 = Queue()
    q1 = deque()
    q2 = deque()

    def __init__(self, arr):
        for item in arr:
            self.q1.put(item)
        while self.q1:
            self.q2.put(self.q1.get())

    def push(self, num):
        while self.q2:
            self.q1.put(self.q2.get())
        self.q1.put(num)
        while self.q1:
            self.q2.put(self.q1.get())
        print(self.q2)

    def pop(self):
        return self.q2.get()


arr = [1, 3, 5, 7, 9]
st = stack(arr)
st.push(2)
print(st.pop())