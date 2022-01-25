#https://www.acmicpc.net/problem/1246

import math

pl = []
n, m = map(int, input().split())
if 1 <= m <= 1000 and 1 <= n <= 1000:
    for i in range(m):
        pi = int(input())
        pl.append(pi)
    pl = sorted(pl, reverse=True)

    price = 0
    max_price = 0

    for i in range(m):
        if i + 1 > n:
            profit = pl[i] * n
        else:
            profit = pl[i] * (i + 1)

        if max_price < profit:
            price = pl[i]
            max_price = profit

    print(price, max_price)