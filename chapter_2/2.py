def func(m, n):

    for num_chickens in range(m + 1):
        num_rabbits = m - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == n:
            return num_chickens, num_rabbits
    return None


total_heads = 20
total_legs = 56

result = func(total_heads, total_legs)
if result:
    num_chickens, num_rabbits = result
    print(f"Number of chickens: {num_chickens}")
    print(f"Number of rabbits: {num_rabbits}")
else:
    print("No solution found.")
