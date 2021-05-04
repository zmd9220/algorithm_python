from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    q = deque(truck_weights)
    bridge_weight = 0
    bridge_truck = deque()
    while True:
        # 현재 다리가 버틸 수 있는 무게 보다 작거나 같은 트럭이 오면 추가하고 건너게함 -
        # bridge_truck에 들어갈 수 있는 횟수는 총 n번 = o(n) 그리고 pop, append, += 연산 시간 = o(1) => o(n)
        if q and bridge_weight + q[0] <= weight:
            now_truck = q.popleft()
            bridge_truck.append([now_truck, 0])
            bridge_weight += now_truck
        # 현재 다리를 건너고 있는 트럭들에 대해 매 시간 마다 거리만큼인 +1을 해줌 - 시간이 제일 많이 걸리는 부분
        for i in range(len(bridge_truck)):
            bridge_truck[i][1] += 1
        # 현재 트럭이 다리를 다 건넜으면 건넌 트럭들은 모두 꺼냄(동시에 여러 트럭이 도착 할 수도 있음) - 위와 같은 o(n)
        while bridge_truck and bridge_truck[0][1] == bridge_length:
            bridge_weight -= bridge_truck[0][0]
            bridge_truck.popleft()
        # 모든 작업이 끝나면 시간 +1
        answer += 1
        if not q and not bridge_truck:
            break
    return answer

length = 100
w = 100
trucks = [10]
print(solution(length, w, trucks))

# import queue
# def solution(bridge_length, weight, truck_weights):
#     timeline=queue.Queue()
#     S=0
#     t=0
#     for _ in range(bridge_length-1):
#         timeline.put(0)
#     for truck in truck_weights:
#         if S+truck <= weight:
#             S+=truck-timeline.get()
#             t+=1
#             timeline.put(truck)
#         else:
#             while S+truck > weight:
#                 S-=timeline.get()
#                 t+=1
#                 timeline.put(0)
#             S+=truck-timeline.get()
#             timeline.put(truck)
#             t+=1
#     return t+bridge_length


# import collections

# DUMMY_TRUCK = 0


# class Bridge(object):

#     def __init__(self, length, weight):
#         self._max_length = length
#         self._max_weight = weight
#         self._queue = collections.deque()
#         self._current_weight = 0

#     def push(self, truck):
#         next_weight = self._current_weight + truck
#         if next_weight <= self._max_weight and len(self._queue) < self._max_length:
#             self._queue.append(truck)
#             self._current_weight = next_weight
#             return True
#         else:
#             return False

#     def pop(self):
#         item = self._queue.popleft()
#         self._current_weight -= item
#         return item

#     def __len__(self):
#         return len(self._queue)

#     def __repr__(self):
#         return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


# def solution(bridge_length, weight, truck_weights):
#     bridge = Bridge(bridge_length, weight)
#     trucks = collections.deque(w for w in truck_weights)

#     for _ in range(bridge_length):
#         bridge.push(DUMMY_TRUCK)

#     count = 0
#     while trucks:
#         bridge.pop()

#         if bridge.push(trucks[0]):
#             trucks.popleft()
#         else:
#             bridge.push(DUMMY_TRUCK)

#         count += 1

#     while bridge:
#         bridge.pop()
#         count += 1

#     return count


# def main():
#     print(solution(2, 10, [7, 4, 5, 6]), 8)
#     print(solution(100, 100, [10]), 101)
#     print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


# if __name__ == '__main__':
#     main()