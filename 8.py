def fibonacci_series(n):
    """
    This function prints the first n terms of a Fibonacci series.
    """
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Sample usage:
n = 10
fibonacci_series(n)
