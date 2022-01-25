#https://www.acmicpc.net/problem/2941

text = input()
if 0 < len(text) <= 100:
    cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for c in cro:
        text = text.replace(c, '!')
    print(len(text))