"""A = [(0, 0), (1, 1), (1, 2)]
count = 0
for i in range(0, len(A)-1):
    s1 = abs(A[i][0] - A[i+1][0])
    s2 = abs(abs(A[i][1] - A[i+1][1]) - s1)
    count = count + s1 + s2
    print("count = ", count)
print(count)"""

A = [0, 1, 1]
B = [0, 1, 2]
count = 0
for i in range(0, len(A)-1):
    s1 = abs(A[i+1] - A[i])
    s2 = abs(abs(B[i+1] - B[i]) - s1)
    count = count + s1 + s2

print(count)