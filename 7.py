def gcd(a, b):
    """
    This function returns the greatest common divisor of two integers using Euclid's algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    """
    This function checks whether two integers are co-prime or not.
    """
    return gcd(a, b) == 1

# Sample usage:
a = 14
b = 25

if are_coprime(a, b):
    print(f"{a} and {b} are co-prime.")
else:
    print(f"{a} and {b} are not co-prime.")
