n = int(input())


def fibonacci(n):
    if n < 2:
        return n
    if memo[n] is None:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]


memo = [None] * 91
print(fibonacci(n))