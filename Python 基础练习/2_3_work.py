res = []

for i in range(100):
    res.append(i)

sum = 0

for i in res:
    if i % 3 == 0:
        sum += i
        print(i)
