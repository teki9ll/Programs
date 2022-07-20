A = 1123
res = list(map(int, str(A)))
pr = res[0]
if 0 in res:
    print(0)
else:
    for i in range(1, len(res)):
        pr = pr * res[i]
    print(pr)
