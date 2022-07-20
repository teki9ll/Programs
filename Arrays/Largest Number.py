A = [3, 30, 34, 5, 9]
A = list(map(str, A))
A.sort(reverse=True)
st = []
print(A)
i = 0
while i < len(A)-1:
    print(i)
    if A[i] < A[i+1]:
        st.append(str(max(int(A[i] + A[i+1]), int(A[i+1] + A[i]))))
        print(st)
        i += 2
    else:
        st.append(A[i])
        i += 1
    print(st)

st = ''.join(st)
print(st)