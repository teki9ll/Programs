def lenLast(A):
    n = len(A) - 1
    count = 0
    if n == -1:
        return 0
    while (A[n] != ' '):
        count += 1
        n -= 1
    return count


x = lenLast("asda asdasd")
print(x)

