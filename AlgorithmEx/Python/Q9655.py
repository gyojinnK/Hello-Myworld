#https://www.acmicpc.net/problem/9655

n = int(input())
if 1 <= n <= 1000:
    if n % 2 == 0:
        print('CY')
    else:
        print('SK')