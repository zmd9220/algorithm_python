
class Queue:
    arr = [0] * 10
    front = 0
    rear = -1

    def enqueue(self, num):
        if self.isFull():
            return 'queue is full'
        else:
            self.rear += 1
            self.arr[self.rear] = num

    def isEmpty(self):
        return self.front-1 == self.rear

    def isFull(self):
        return self.rear == (len(self.arr)-1)

    def dequeue(self):
        if self.isEmpty():
            return 'queue is empty'
        else:
            pop = self.arr[self.front]
            self.front += 1
            return pop

    def qpeek(self):
        if self.isEmpty():
            return 'queue is empty'
        else:
            return self.arr[self.front]


test = Queue()
test.enqueue(1)
print(test.arr)
test.enqueue(2)
print(test.arr)
test.enqueue(3)
print(test.arr)
print(test.dequeue())
# print(test.front)
print(test.dequeue())
# print(test.front)
print(test.dequeue())
# print(test.front)
