def process(n):
    ans = sum(1 / (step * (i + 1)) for i, step in enumerate(range(1, n + 1)))
    return ans


n = int(input())

result = process(n)

print(result)
