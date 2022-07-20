A = [0.6, 0.7, 0.8, 1.2, 0.4]
A = [float(i) for i in A]
A.sort()
for i in range(0, len(A)):
    for j in range(i + 1, len(A)):
        for k in range(j + 1, len(A)):
            if 1 < (A[i] + A[j] + A[k]) < 2:
                print(1)
print(0)

# this is the bruteforce
# try array bucketing