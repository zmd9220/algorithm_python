# MST는 프림, 크루스칼이 대표적인 알고리즘

def find_set(num):
    while set_arr[num] != num:
        num = set_arr[num]
    return num

def union(base_el, change_el):
    set_arr[find_set(change_el)] = find_set(base_el)


def kruskal():
    sorting_edges = sorted(edges, key=lambda x: -x[2])
    # print(sorting_edges)
    mst = []  # 간선 수(가중치만 넣어도 되고, 시작,종점,가중치 다 넣어도되고.. 자유)

    # 종료 조건 선택된 간선수 = 정점수 -1 or 사용된 정점수 = 제시된 정점수
    while len(mst) != v:
        start_v, dst_v, weight = sorting_edges.pop()
        if find_set(start_v) != find_set(dst_v):
            union(start_v, dst_v)
            mst.append(weight)

    # vertices = set()  # 사용된 정점 (둘 다 사용되고 있는 정점인지 체크용)
    # 종료 조건 선택된 간선수 = 정점수 -1 or 사용된 정점수 = 제시된 정점수
    # while len(vertices) != v+1:
    #     start_v, dst_v, weight = sorting_edges.pop()
    #     # 둘 다 사용된 정점에 있는 경우만 제외 둘 중 하나만 사용중이면 ok, 둘다 안쓰여도 ok
    #     if start_v not in vertices or dst_v not in vertices:
    #         # mst.append((start_v, dst_v, weight))
    #         mst.append(weight)
    #         vertices.add(start_v)
    #         vertices.add(dst_v)
    #     print(vertices)
    return mst


for t in range(int(input())):
    v, e = map(int, input().split())
    set_arr = [i for i in range(v+1)]
    edges = [list(map(int, input().split())) for _ in range(e)]
    ans = kruskal()
    print('#{} {}'.format(t+1, sum(ans)))
