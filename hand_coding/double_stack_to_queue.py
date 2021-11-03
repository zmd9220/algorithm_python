class queue():
    st = []
    st2 = []

    def __init__(self, input):
        for item in input:
            self.st.append(item)
        while self.st:
            self.st2.append(self.st.pop())

    def enqueue(self, num):
        self.st.append(num)
        while self.st2:
            self.st.append(self.st2.pop())
        while self.st:
            self.st2.append(self.st.pop())

    def dequeue(self):
        if self.st2:
            return self.st2.pop()
        else:
            return 'Empty'