#https://www.acmicpc.net/problem/1037

n = []
A = 0
nc = int(input())
if 0 < nc <= 50:
    m = 0
    n = list(map(int, input().split()))
    n.sort()
    for i in n:
        if 1 < i and i != (i+1) or i % 2 == 0:
            A = n[0] * n[nc-1]
    print(A)