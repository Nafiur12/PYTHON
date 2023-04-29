n = int(input("Enter the number of terms you want to generate: "))

# initialize first two terms
fibonacci_series = [0, 1]
sum_of_fibonacci = 1

# generate fibonacci series and add to sum
for i in range(2, n):
    fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
    sum_of_fibonacci += fibonacci_series[i]

# print the fibonacci series and its sum
print("Fibonacci series:", fibonacci_series)
print("Sum of Fibonacci series:", sum_of_fibonacci)
