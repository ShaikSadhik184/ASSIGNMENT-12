# function to find gcd of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# function to find lcm of two numbers
def lcm(a, b):
    return (a*b)//gcd(a,b)

# take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# find lcm and print the result
print("LCM of", num1, "and", num2, "is", lcm(num1, num2))
