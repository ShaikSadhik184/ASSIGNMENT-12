def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

# Example usage
print(next_prime(7))  # Output: 11
