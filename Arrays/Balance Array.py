A = [ 2, 1, 6, 4 ]
even = []
odd = []
for i in range(0, len(A)):
    if i % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])

print(even , odd)

print(abs(sum(even) - sum(odd)))