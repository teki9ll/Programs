A = "the sky is blue"
A = A.split()

start = 0
end = len(A) - 1

while (start <= end):
    temp = A[start]
    A[start] = A[end]
    A[end] = temp

    start += 1
    end -= 1

print(" ".join(A))