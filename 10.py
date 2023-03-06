# function to find HCF of two numbers
def find_hcf(num1, num2):
    # find smaller number between num1 and num2
    smaller = min(num1, num2)
    hcf = 1
    # iterate from 1 to smaller and find factors that divide both numbers
    for i in range(1, smaller+1):
        if num1%i == 0 and num2%i == 0:
            hcf = i
    return hcf

# get user input for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# call function to find HCF and print result
hcf = find_hcf(num1, num2)
print("HCF of", num1, "and", num2, "is", hcf)
