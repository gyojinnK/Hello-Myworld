#https://www.acmicpc.net/problem/1251

m = 3
tex = list(input().strip())
f_tex = []
f_ans = []
tl = len(tex)
if 3 <= len(tex) <= 50:
    for i in range(1, len(tex)-1):
        for j in range(i+1, len(tex)):
            t1 = tex[:i]
            t2 = tex[i:j]
            t3 = tex[j:]
            t1.reverse()
            t2.reverse()
            t3.reverse()
            f_tex.append(t1 + t2 + t3)
    for i in f_tex:
        f_ans.append(''.join(i))
    f_ans.sort()
    print(f_ans[0])