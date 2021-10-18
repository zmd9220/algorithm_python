from collections import defaultdict, deque


def dfs(dic, route, length):
    if len(route) == length:
        pass
    for i in range(len(dic[route[-1]])):
        tmp = dic[route[-1]].pop()
        route.append(tmp)
        dfs(dic, tmp)
        route.pop()
        dic[route[-1]].append(tmp)


def dfs2(dic, route):
    answer = []
    st = [['ICN']]
    while st:
        tmp = st.pop()
        if len(tmp) == 6:
            pass


def solution(tickets):
    answer = []
    dic = defaultdict(list)
    for ticket in tickets:
        # dic[ticket[0]].setdefault(dic[ticket[0]].append(ticket[1]), [])
        dic[ticket[0]].append([ticket[1], 0])
    # print(dic, len(dic), len(tickets)+1)
    # print('ICN'>'ATL')
    st = [['ICN']]
    while st:
        tmp = st.pop()
        if len(tmp) == len(tickets) + 1:
            answer.append(tmp)
            continue
        for i in range(len(dic[tmp[-1]])):
            if not dic[tmp[-1]][i][1]:
                tmp.append(dic[tmp[-1]][i][0])
                dic[tmp[-1]][i][1] = 1
                st.append(tmp)
                tmp.pop()

    print(answer)
    # dfs(dic, ["ICN"], len(tickets) + 1)

    return answer