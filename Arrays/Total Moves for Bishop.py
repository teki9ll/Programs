'''
A = 4
B = 4
count = 0
for (int i = A, j = B; 1 <= i && i <= 8 && 1 <= j && j <= 8; i++, j++):
    count += 1
for (int i = A, j = B; 1 <= i && i <= 8 && 1 <= j && j <= 8; i++, j--):
    count += 1
for (int i = A, j = B; 1 <= i && i <= 8 && 1 <= j && j <= 8; i--, j--):
    count += 1
for (int i = A, j = B; 1 <= i && i <= 8 && 1 <= j && j <= 8; i--, j++):
    count += 1
print(count - 4)

PSEUDOCODE
'''
