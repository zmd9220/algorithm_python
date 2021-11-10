from queue import Queue
from collections import deque
class stack:
    q1 = Queue()
    q2 = Queue()
    q1 = deque()
    q2 = deque()

    def __init__(self, arr):
        for item in arr:
            self.q1.append(item)
            while self.q2:
                # self.q1.put(self.q2.get())
                self.q1.append(self.q2.popleft())
            # self.q1.put(item)
            # self.q1.append(item)
            print(self.q1)

            while self.q1:
                # self.q2.put(self.q1.get())
                self.q2.append(self.q1.popleft())
            print(self.q2)

    def push(self, num):
        self.q1.append(num)
        while self.q2:
            # self.q1.put(self.q2.get())
            self.q1.append(self.q2.popleft())
        # self.q1.put(num)
        # self.q1.append(num)
        while self.q1:
            # self.q2.put(self.q1.get())
            self.q2.append(self.q1.popleft())
        print(self.q2)

    def pop(self):
        # return self.q2.get()
        return self.q2.popleft()


arr = [1, 3, 5, 7, 9]
st = stack(arr)
st.push(2)
print(st.pop())