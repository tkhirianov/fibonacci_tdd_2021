def fib(n):
    if n < 0:
        raise ValueError("Fibonacci function is not defined for n < 0.")
    if n >= 10000:
        raise ValueError("Fibonacci function contract assumes n < 10000.")
    if n <= 1:
        return n
    f = [0, 1] + [None]*(n - 1)
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
