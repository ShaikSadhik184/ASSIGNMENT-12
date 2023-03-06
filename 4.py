# function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# get user input for range of numbers
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

# loop through the range and print prime numbers
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper+1):
    if is_prime(num):
        print(num)
