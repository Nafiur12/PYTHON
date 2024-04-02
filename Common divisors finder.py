#Write a Python program to find common divisors between two numbers
def find_common_divisors(num1, num2):
    common_divisors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    return common_divisors


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    common_divisors = find_common_divisors(num1, num2)

    if common_divisors:
        print("Common divisors:", common_divisors)
    else:
        print("There are no common divisors between the two numbers.")
