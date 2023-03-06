def is_prime(num):
    """
    Returns True if the given number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    """
    Prints the first n prime numbers.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

# Example usage:
print_primes(10)  # prints the first 10 prime numbers

