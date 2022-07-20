A = 15
ls = []
for i in range(1, A + 1):
    if i % 15 == 0:
        ls.append("FizzBuzz")
    elif i % 3 == 0:
        ls.append("Fizz")
    elif i % 5 == 0:
        ls.append("Buzz")
    else:
        ls.append(i)

print(ls)