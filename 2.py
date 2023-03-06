def is_prime(num):
    # Check if the number is less than 2
    if num < 2:
        return False

    # Loop through numbers from 2 to num-1
    for i in range(2, num):
        # If the number is divisible by i, it's not prime
        if num % i == 0:
            return False
    
    # If the loop completes without finding a factor, the number is prime
    return True


num = 17
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
