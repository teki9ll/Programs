A = "ShubhTej"

a = []
for i in A:
    if i.isupper():
        a.append(i.lower())
    else:
        a.append(i.upper())

print("".join(a))