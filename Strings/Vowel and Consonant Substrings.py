A = 
count = 0
vowel = ['a', 'e', 'i', 'o', 'u']

def consonants(st):
    conso = 0
    for i in st:
        if i not in vowel:
            conso += 1
    return conso

def vowels(st):
    vow = 0
    for i in st:
        if i in vowel:
            vow += 1
    return vow

for i in range(0,len(A)):
    if A[i] in vowel:
        count += consonants(A[i+1:])
    else:
        count += vowels(A[i+1:])

print(count)
