#https://www.acmicpc.net/problem/1343

b = input()
if 0 < len(b) <= 50:
    b = b.replace("XXXX", "AAAA")
    b = b.replace("XX", "BB")
    if 'X' in b:
        print(-1)
    else:
        print(b)