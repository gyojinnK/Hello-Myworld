#https://www.acmicpc.net/problem/1010

import math
T = int(input())
nml = []
while 0 < T:
    n, m = map(int, input().split())
    if 0 < n <= m < 30:
        result = int(math.factorial(m) / (math.factorial(m - n) * math.factorial(n)))
        nml.append(result)
    T = T - 1
for r in nml:
    print(r)