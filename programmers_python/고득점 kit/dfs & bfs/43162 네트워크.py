# from collections import deque
import collections


def bfs(n, computers, visited, num):
    q = collections.deque()
    q.append(num)
    while q:
        now_com = q.popleft()
        for i in range(n):
            if computers[now_com][i] and not visited[i]:
                visited[i] = 1
                q.append(i)
    return


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer += 1
            bfs(n, computers, visited, i)
    return answer