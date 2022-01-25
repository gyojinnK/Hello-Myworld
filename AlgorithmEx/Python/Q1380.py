#https://www.acmicpc.net/problem/1380

ans_stu = []
f_print = []
s_count = 1
while True:
    inp_stu = []
    nl = []
    n = int(input())
    if n == 0:
        break
    for n in range(n):
        name = input()
        inp_stu.append(name)
    for n in range((len(inp_stu)*2)-1):
        number = int(input().split()[0])
        if number in nl:
            nl.remove(number)
            number = 0
        nl.append(number)
    for m in nl:
        if m != 0:
            ans_stu.append(inp_stu[m-1])
    f = f'{ans_stu[0]}'
    f_print.append(f)
    for s in ans_stu:
        ans_stu.remove(s)
for i in range(len(f_print)):
    print(s_count+i, f_print[i])