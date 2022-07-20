A = "the fastest racecar"
A = A.split()
count = 0
for i in A:
    if i == i[::-1]:
        count += 1
print(count)