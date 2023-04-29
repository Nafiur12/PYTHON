# Write and run a python program to find the sum = 1 − 3^2 + 5^2 − .... using the for loop.
num_terms = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, num_terms + 1):
    term = (-1) ** (i+1) * (2*i - 1) ** 2
    sum += term
print("The sum of the series is", sum)
