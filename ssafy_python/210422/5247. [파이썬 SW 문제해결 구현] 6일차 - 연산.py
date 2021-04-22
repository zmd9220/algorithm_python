# 이 문제 시간 초과 때문에 일반 리스트로는 힘듬
# 파이썬 제공 라이브러리인 deque 사용하거나
# 직접 원형큐 구현해서 계산하는 수 밖에 없다. - 어제 라이브에서 말한 c 방식으로 인덱스 직접접근하여 시간 줄이기
from collections import deque

q_size = 1000001
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.data = [0] * q_size

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % q_size

    def queueReset(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % q_size
            self.data[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % q_size
            return self.data[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.data[(self.front + 1) % q_size]

    def print(self):
        out = []
        if self.front < self.rear:
            out = self.data[self.front+1:self.rear+1]
        else:
            out = self.data[self.front+1:q_size] + self.data[0:self.rear+1]

        print("[f=%s, r=%d] ==> "%(self.front, self.rear), out)


def bfs(start_val, dst_val):
    # q = [(start_val, 0)]
    q = deque()
    q.append((start_val, 0))
    # visited 는 필요없을듯 중복연산이라 X
    # visited를 각 수로 해야함 수 2번을 방문했으면 수 visited[2] = 1
    # 왜냐면 2를 재방문해도 이미 전에 2를 넣고 계산하고 있는 데이터가 안에 돌고 있기 때문에 다시 넣을 필요가 없기 때문이다.
    # visited = [0] * 1000001
    visited_dict = {}
    while q:
        now_val, cnt = q.popleft()
        # 현재 들어온 수가 이미 먼저 계산되어 나왔던 수인지 찾기 이미 들어왔으면 패스, 아니면 체크
        if visited_dict.get(now_val, 0):
            continue
        visited_dict[now_val] = 1
        # if visited[now_val] == 1:
        #     continue
        # else:
        #     visited[now_val] = 1
        # 탈출 조건
        if now_val == dst_val:
            return cnt
        # 4가지 +1, -1, *2, -10
        if 0 < now_val - 1 <= 1000000:
            q.append((now_val - 1, cnt + 1))
        if 0 < now_val - 10 <= 1000000:
            q.append((now_val - 10, cnt + 1))
        if 0 < now_val + 1 <= 1000000:
            q.append((now_val+1, cnt+1))
        if 0 < now_val * 2 <= 1000000:
            q.append((now_val*2, cnt+1))


def bfs2(start_val, dst_val):
    # q = [(start_val, 0)]
    q = CircularQueue()
    q.enqueue((start_val, 0))
    # print(q.data[1], q.data[0])
    # visited 는 필요없을듯 중복연산이라 X
    # visited를 각 수로 해야함 수 2번을 방문했으면 수 visited[2] = 1
    # 왜냐면 2를 재방문해도 이미 전에 2를 넣고 계산하고 있는 데이터가 안에 돌고 있기 때문에 다시 넣을 필요가 없기 때문이다.
    # visited = [0] * 1000001
    visited_dict = {}
    while q:
        now_val, cnt = q.dequeue()
        # 현재 들어온 수가 이미 먼저 계산되어 나왔던 수인지 찾기 이미 들어왔으면 패스, 아니면 체크
        if visited_dict.get(now_val, 0):
            continue
        visited_dict[now_val] = 1
        # if visited[now_val] == 1:
        #     continue
        # else:
        #     visited[now_val] = 1
        # 탈출 조건
        if now_val == dst_val:
            return cnt
        # 4가지 +1, -1, *2, -10
        if 0 < now_val - 1 <= 1000000:
            q.enqueue((now_val - 1, cnt + 1))
        if 0 < now_val - 10 <= 1000000:
            q.enqueue((now_val - 10, cnt + 1))
        if 0 < now_val + 1 <= 1000000:
            q.enqueue((now_val+1, cnt+1))
        if 0 < now_val * 2 <= 1000000:
            q.enqueue((now_val*2, cnt+1))


for t in range(int(input())):
    n, m = map(int, input().split())
    ans = bfs(n, m)
    # ans = bfs2(n, m)
    print('#{} {}'.format(t+1, ans))
