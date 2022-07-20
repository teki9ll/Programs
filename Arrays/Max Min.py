A = [1, 2, 3]

num = int("".join([str(i) for i in A]))
num = num + 1
num = [int(x) for x in str(num)]

print(num)