#https://www.acmicpc.net/problem/7568

N = int(input())
w_l = []
h_l = []
score = []
if 2 <= N <= 50:
    for n in range(N):
        wei, hei = map(int, input().split())
        w_l.append(wei)
        h_l.append(hei)
    for i in range(N):
        k = 0
        for j in range(N):
            if i != j:
                if w_l[i] < w_l[j] and h_l[i] < h_l[j]:
                    k = k + 1
        score.append(k+1)
    for s in score:
        print(s)
