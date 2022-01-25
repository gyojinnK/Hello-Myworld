#https://www.acmicpc.net/problem/1181

cl = []
t = 0
t2 = 0
n = int(input())
if 1 <= n <= 20000:
    for i in range(n):
        c = input()
        cl.append(c)
    cl2 = set(cl)
    cl = list(cl2)
    cl.sort()
    cl.sort(key=len)
    for i in cl:
        print(i)