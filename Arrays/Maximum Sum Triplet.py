A = [2, 5, 3, 1, 4, 9]
count = -1000000
if len(A) >= 3:
    for i in range(0,len(A)):
        if A[i+1] >= A[i]:
            for j in range(i,len(A)):
                if A[j+1] >= A[j]:
                    for k in range(k,len(A)):
                        if count < A[i] + A[j] + A[k]:
                            count = A[i] + A[j] + A[k]
    print(count)
else:
    print(count)