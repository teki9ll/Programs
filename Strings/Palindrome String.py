A = "pGpEusuCSWEa"
A = A.lower()
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in range(0,len(A)):
    if A[i] in vowel:
        count = count + (len(A) - i)

print(count%10003)