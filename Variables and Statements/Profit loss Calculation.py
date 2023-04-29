# Python program to print Fibonacci series up to n terms

# Function to print Fibonacci sequence
def fib(n):
    # First two terms of Fibonacci sequence
    a, b = 0, 1
    # Loop to print Fibonacci sequence up to n terms
    for i in range(n):
        print(a)
        a, b = b, a + b

# Main function
if __name__ == '__main__':
    # Take user input for number of terms
    n = int(input("Enter the number of terms: "))
    # Call function to print Fibonacci sequence
    fib(n)
