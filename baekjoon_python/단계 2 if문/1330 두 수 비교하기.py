# a = int(input())
# b = int(input())
c, d = input().split()
a = int(c)
b = int(d)
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")
