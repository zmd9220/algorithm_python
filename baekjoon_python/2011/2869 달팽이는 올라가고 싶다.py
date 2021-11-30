
'''
해당하는 곳을 넘기위한 최소한의 위치 = v-a 보다 같거나 크면 무조건 그 다음은(+1) 도착

'''
a, b, v = map(int, input().split())
last_meter = v-a
day_meter = a-b
last_day = (last_meter // day_meter) + 1 if last_meter % day_meter else last_meter // day_meter
print(last_day+1)

# cnt = 0
# now = 0
# while True:
#     now += a
#     cnt += 1
#     if now >= v:
#         break
#     else:
#         now -= b
# print(cnt)
# tmp = v // (a-b)
# mod = divmod(v, (a-b))
# print(v//(a-b))