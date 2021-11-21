from collections import deque, OrderedDict


def bfs(now_word, target, words, visited, cnt):
    if now_word == target:
        global answer
        # print(answer)
        if not answer or answer > cnt:
            answer = cnt
            return
    for j in range(len(now_word)):
        for k in range(26):
            tmp = list(now_word)
            tmp[j] = chr(ord('a') + k)
            tmp = ''.join(tmp)
            if tmp in words and not visited[tmp]:
                visited[tmp] = 1
                bfs(tmp, target, words, visited, cnt + 1)
                visited[tmp] = 0


def solution(begin, target, words):
    ans = 0
    if target not in words:
        return 0
    # visited = [0] * len(words)
    visited = OrderedDict()
    for i in range(len(words)):
        visited[words[i]] = 0
        if words[i] == begin:
            visited[words[i]] = 1
    bfs(begin, target, words, visited, 0)
    global answer
    ans = answer
    answer = 0
    return ans


answer = 0
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))