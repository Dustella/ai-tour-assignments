res = []

for i in range(10):
    content = input()
    res.append(int(content))

msg = " ".join([str(i) for i in res])
print(msg)
print(f"avergae: {sum(res)/len(res)}")

count_over_average = 0

for i in res:
    if i > sum(res)/len(res):
        count_over_average += 1

print(f"over average count: {count_over_average}")

# sort res
res.sort(reverse=True)

# output sorted res
msg = " ".join([str(i) for i in res])
print(f"sorted res: {msg}")
