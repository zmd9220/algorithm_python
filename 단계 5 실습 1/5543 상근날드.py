import sys

burger = 3000
drink = 3000
for i in range(3):
    a = int(sys.stdin.readline().rstrip())
    if a < burger:
        burger = a

for i in range(2):
    a = int(sys.stdin.readline().rstrip())
    if a < drink:
        drink = a
print(burger + drink - 50)